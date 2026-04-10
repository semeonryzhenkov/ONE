import csv
import json

d = {}

with open('observe.csv', 'r') as f:
    r = csv.DictReader(f, delimiter=';')
    for row in r:
        p = row['place']
        dur = int(row['duration'])
        rel = int(row['reliability'])
        hgt = int(row['height'])

        if p not in d:
            d[p] = {'duration': 0, 'reliability': -1, 'height': float('inf')}

        d[p]['duration'] += dur
        if rel > d[p]['reliability']:
            d[p]['reliability'] = rel
        if hgt < d[p]['height']:
            d[p]['height'] = hgt

with open('reality.json', 'w') as f:
    json.dump(d, f, indent=4, sort_keys=True)
