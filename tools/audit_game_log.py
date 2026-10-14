"""Summarize an existing HOI4 error log without modifying the user's logs."""
import argparse,json,re
from collections import Counter
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--log',type=Path,default=Path.home()/'Documents/Paradox Interactive/Hearts of Iron IV/logs/error.log')
p.add_argument('--output',type=Path,default=Path(__file__).resolve().parents[1]/'docs/game_log_audit.json')
a=p.parse_args();lines=a.log.read_text(encoding='utf-8-sig',errors='replace').splitlines()
patterns={
 'turkish_advisor_token':'TUR_recep_peker is not A valid Idea',
 'empty_small_icon':'Icon definition "_small"',
 'event_id_parse':r'Malformed token|Expected start of list reading CID',
 'numeric_focus_token':r'Creation of dynamic token',
 'focus_shine':r'Missing icon shine for focus',
 'missing_turkish_tree':r'Unable to find focus tree with ID: turkish_focus',
 'localization_collision':r'loc key collisions',
 'core_resistance':r'initializing resistance for a core state',
 'unknown_character':r'recruit_character: Unknown character',
 'german_equipment':r'Country "GER" does not have any equipment variant',
 'german_division_names':r'GER -> Group name:',
 'other_mod_versions':r'Invalid supported_version',
 'session_commands':r'Dropped command:',
 'sound_duplicates':r'Sound.*already|SoundEffect.*already|Could not load sound file',
}
counts={k:sum(bool(re.search(pattern,line)) for line in lines) for k,pattern in patterns.items()}
repeat=Counter(re.sub(r'^\[[^]]*\]\[[^]]*\]','',line) for line in lines)
report={'log':str(a.log),'total_lines':len(lines),'modified':a.log.stat().st_mtime,'categories':counts,'most_repeated':repeat.most_common(20)}
a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Log lines:',len(lines));print(json.dumps(counts,ensure_ascii=False,indent=2));print('Saved:',a.output)
