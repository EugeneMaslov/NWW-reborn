"""Capture the current atlas UI for README using the same local browser as atlas QA."""
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT = Path(__file__).resolve().parents[1]
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument('--window-size=1600,1000')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
service = Service('C:/Users/Eugene/.cache/selenium/chromedriver/win64/154.0.8037.92/chromedriver.exe',
                  service_args=['--disable-build-check'])
driver = webdriver.Chrome(service=service, options=options)
try:
    driver.get((ROOT / 'sites/nww-atlas/dist/index.html').as_uri())
    # Overseas possessions make whole-country bounding boxes global. Use mainland Europe/West Asia.
    driver.execute_script('''
      view=[2450,100,1750,1150];applyView();
    ''')
    target = ROOT / 'docs/art/readme/nww-content-map.png'
    target.parent.mkdir(parents=True, exist_ok=True)
    driver.save_screenshot(str(target))
    print(target)
finally:
    driver.quit()
