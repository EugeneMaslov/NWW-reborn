"""Include early Bohemian access and service reforms in each existing GER route."""
import json
from pathlib import Path
from hoi4_script import read,one,parse,dump

ROOT=Path(__file__).resolve().parents[1]


def main():
    path=ROOT/'common/ai_strategy_plans/GER_historical.txt'
    doc=read(path)
    specs=json.loads((ROOT/'docs/GER_services_expansion.json').read_text(encoding='utf-8'))['new_focuses']
    for name,plan,o in doc:
        if not isinstance(plan,list):continue
        order=one(plan,'ai_national_focuses')
        opening=['GER_the_gilded_colossus','GER_the_kaiser_endures','GER_guardians_of_the_reich','GER_nww_prague_network','GER_prussian_traditions']
        old=[v for k,v,o in order if v not in opening]
        industrial='GER_nww_civil_investment' if name.endswith('democratic') else 'GER_nww_defence_procurement'
        school='GER_nww_deliberate_battle' if name.endswith('democratic') else 'GER_nww_mission_command'
        opposite='GER_nww_defence_procurement' if industrial.endswith('civil_investment') else 'GER_nww_civil_investment'
        opposite_school='GER_nww_mission_command' if school.endswith('deliberate_battle') else 'GER_nww_deliberate_battle'
        # Dated diplomatic goals stay ahead of the development tail, so new
        # service content fills waiting time without delaying a ready objective.
        additions=[s['id'] for s in specs if s['id'] not in (opposite,opposite_school)]
        order[:]=[(None,f,None) for f in dict.fromkeys(opening+old+additions)]
        factors=one(plan,'focus_factors',None)
        if factors is None:factors=[];plan.append(('focus_factors',factors,'='))
        for key in (opposite,opposite_school):
            factors[:]=[e for e in factors if e[0]!=key];factors.append((key,'0','='))
    path.write_text(dump(doc)+'\n',encoding='utf-8',newline='\n')


if __name__=='__main__':main()
