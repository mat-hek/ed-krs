from urllib.request import urlopen
import json
import csv
from pprint import pprint

with open('csv/relations.csv', 'w') as relations_f, \
     open('csv/people.csv', 'w') as people_f, \
     open('csv/subjects.csv', 'w') as subjects_f:
    [relations, people, subjects] = [csv.writer(f) for f in [relations_f, people_f, subjects_f]]
    people.writerow(['id', 'last_name', 'first_name', 'second_names', 'gender'])
    subjects.writerow(['id', 'name', 'krs_id', 'legal_form', 'legal_form_id'])
    relations.writerow(['subject_id', 'subject_krs_id', 'person_id'])
    for page in range(1, 200):
        with open('krs_dump/page_{}.json'.format(page), 'r') as file:
            data = json.load(file)
            for d in data['items']:
                dd = d['data']
                if d['class'] == 'Person':
                    people.writerow([dd['krs_id'], dd['last_name'], dd['first_name'], dd['second_names'], d['items']['registries']['krs']['data']['plec']])
                elif d['class'] == 'KrsOrganization':
                    subjects.writerow([d['global_id'], dd['nazwa'], dd['id'], dd['forma_prawna_str'], dd['forma_prawna_id']])
                    for p in dd.get('person_id', []):
                        relations.writerow([d['global_id'], dd['id'], p])
                else:
                    pprint(d)
