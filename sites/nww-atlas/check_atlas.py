"""Browser checks for the generated offline atlas. Requires Selenium/Chrome."""
import json
from pathlib import Path
import random
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image
import csv

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from build_content_atlas import effective, initial_owner
from hoi4_script import one, read

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument('--window-size=1440,1000')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
service = Service('C:/Users/Eugene/.cache/selenium/chromedriver/win64/154.0.8037.92/chromedriver.exe',
                  service_args=['--disable-build-check'])
driver = webdriver.Chrome(service=service, options=options)
driver.set_script_timeout(60)
try:
    driver.get((ROOT / 'sites/nww-atlas/dist/index.html').as_uri())
    assert driver.title == 'NWW Reborn — Атлас разработки'
    assert driver.execute_script('return paths.length') == 79
    assert driver.find_element(By.ID, 'count-full').text == '10'
    snapshot = driver.execute_script('return DATA.snapshotDate')
    assert '.'.join(reversed(snapshot.split('-'))) in driver.find_element(By.CSS_SELECTOR, '.sidebar-footer').text
    assert driver.execute_script('return DATA.states.find(s => s.state === 762).owner') == 'GER'
    for tag, count in [('FRA', 146), ('ENG', 153), ('MKN', 182), ('POL', 80)]:
        country = driver.execute_script('return byTag.get(arguments[0])', tag)
        assert country['status'] == 'full' and country['focuses'] == count, country
        assert driver.execute_script("return $('country-'+arguments[0]).dataset.status", tag) == 'full'
    driver.find_element(By.ID, 'about-open').click()
    about_text = driver.find_element(By.ID, 'about').text
    assert 'ENG' in about_text and 'FRA' in about_text
    assert 'текущая новая разработка FRA' not in about_text
    driver.find_element(By.ID, 'about-done').click()
    driver.find_element(By.ID, 'search').send_keys('LTB')
    assert len(driver.find_elements(By.CSS_SELECTOR, '.country-row')) == 1
    driver.find_element(By.CSS_SELECTOR, '.country-row').click()
    assert driver.find_element(By.ID, 'detail-name').text == 'Литовско-Белорусский Союз'
    assert driver.find_element(By.ID, 'detail-focuses').text == '96'
    before = driver.execute_script("return svg.getAttribute('viewBox')")
    driver.find_element(By.ID, 'zoom-in').click()
    assert driver.execute_script("return svg.getAttribute('viewBox')") != before
    driver.find_element(By.ID, 'reset').click()
    driver.find_element(By.CSS_SELECTOR, '[data-filter="legacy"]').click()
    assert driver.execute_script('return paths.filter(p=>!p.classList.contains("dim")).length') == 2
    driver.find_element(By.ID, 'search').clear()
    driver.execute_script("$('search').dispatchEvent(new Event('input'))")
    assert len(driver.find_elements(By.CSS_SELECTOR, '.country-row')) == 2
    driver.find_element(By.CSS_SELECTOR, '[data-filter="all"]').click()
    driver.find_element(By.ID, 'search').send_keys('BYE')
    driver.find_element(By.CSS_SELECTOR, '.country-row').click()
    assert 'отсутствует' in driver.find_element(By.ID, 'detail-note').text
    driver.find_element(By.ID, 'about-open').click()
    assert driver.execute_script("return $('about').open")
    driver.find_element(By.ID, 'about-done').click()
    driver.find_element(By.CSS_SELECTOR, '.brand').click()
    exported = driver.execute_async_script('''
      const done=arguments[0],original=URL.createObjectURL,click=HTMLAnchorElement.prototype.click;
      let captured;
      URL.createObjectURL=blob=>{captured=blob;return 'blob:atlas-check';};
      HTMLAnchorElement.prototype.click=function(){};
      downloadSvg();URL.createObjectURL=original;HTMLAnchorElement.prototype.click=click;
      captured.text().then(source=>{
        const doc=new DOMParser().parseFromString(source,'image/svg+xml');
        done({paths:doc.querySelectorAll('path[data-tag]').length,
          germany:doc.querySelector('#country-GER').getAttribute('fill'),
          hungary:doc.querySelector('#country-HUN').getAttribute('fill'),
          legend:doc.documentElement.textContent.includes('Полная переработка'),
          viewBox:doc.documentElement.getAttribute('viewBox')});
      });
    ''')
    assert exported == {'paths':79,'germany':'#63ad72','hungary':'#e6a15a',
                        'legend':True,'viewBox':'0 0 5632 2228'}, exported
    driver.save_screenshot(str(ROOT / 'sites/nww-atlas/preview-desktop.png'))
    driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {
        'width': 390, 'height': 844, 'deviceScaleFactor': 1, 'mobile': True})
    assert driver.execute_script('return document.documentElement.scrollWidth <= innerWidth')
    driver.save_screenshot(str(ROOT / 'sites/nww-atlas/preview-mobile.png'))
    # Rasterize the SVG with one unique color per owner and compare 2,000 pixels
    # against ownership derived directly from province.bmp and effective state files.
    game = Path('D:/Steam/steamapps/common/Hearts of Iron IV')
    owners = {}
    for path in effective(game, 'history/states'):
        state = one(read(path), 'state')
        owner = initial_owner(one(state, 'history', []))
        for _, pid, _ in one(state, 'provinces', []):
            owners[int(pid)] = owner
    color_owner = {}
    with (game / 'map/definition.csv').open(encoding='utf-8-sig') as stream:
        for row in csv.reader(stream, delimiter=';'):
            if row and row[0].isdigit():
                color_owner[tuple(map(int,row[1:4]))] = owners.get(int(row[0])) if row[4] == 'land' else None
    image = Image.open(game / 'map/provinces.bmp').convert('RGB')
    rng = random.Random(1936)
    samples = [(rng.randrange(image.width),rng.randrange(image.height)) for _ in range(2000)]
    expected = [color_owner.get(image.getpixel(point)) for point in samples]
    actual = driver.execute_async_script('''
      const samples=arguments[0],done=arguments[1],clone=svg.cloneNode(true);
      clone.setAttribute('width',DATA.width);clone.setAttribute('height',DATA.height);
      clone.setAttribute('viewBox',`0 0 ${DATA.width} ${DATA.height}`);
      clone.querySelector('.ocean').setAttribute('fill','#000000');
      const tags=[null];
      clone.querySelectorAll('path[data-tag]').forEach((p,i)=>{
        tags.push(p.dataset.tag);p.removeAttribute('class');
        p.setAttribute('fill','#'+(i+1).toString(16).padStart(6,'0'));
        p.setAttribute('stroke','none');
      });
      const img=new Image();img.onload=()=>{
        const canvas=document.createElement('canvas');canvas.width=DATA.width;canvas.height=DATA.height;
        const ctx=canvas.getContext('2d');ctx.drawImage(img,0,0);
        const data=ctx.getImageData(0,0,canvas.width,canvas.height).data;
        done(samples.map(([x,y])=>{const pos=(y*canvas.width+x)*4;return tags[(data[pos]<<16)+(data[pos+1]<<8)+data[pos+2]]??null;}));
      };img.onerror=()=>done({error:'svg rasterization failed'});
      img.src='data:image/svg+xml;charset=utf-8,'+encodeURIComponent(new XMLSerializer().serializeToString(clone));
    ''', samples)
    assert actual == expected, [(samples[i],a,b) for i,(a,b) in enumerate(zip(actual,expected)) if a!=b][:20]
    errors = [e for e in driver.get_log('browser') if e['level']=='SEVERE']
    assert not errors, errors
    print(json.dumps({'browser':'Chrome headless','controls':'passed','svg_export':'passed','mobile_overflow':False,
                      'ownership_pixels_matched':len(samples),'console_errors':len(errors)}))
finally:
    driver.quit()
