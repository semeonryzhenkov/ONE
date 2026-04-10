import json
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)


def load_data():
    data = []
    with open('horror.jsonl', 'r') as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
    return data


@app.route('/aliens/<int:d>/')
def get_aliens(d):
    data = load_data()
    conn = sqlite3.connect('races.db')
    c = conn.cursor()
    c.execute('SELECT race, mouth, front_eyes, back_eyes, tentacles, limbs FROM Aliens')
    rows = c.fetchall()
    conn.close()

    races = set()
    keys = ['mouth', 'front_eyes', 'back_eyes', 'tentacles', 'limbs']

    for item in data:
        if item.get('disgust') == d:
            for row in rows:
                race_name = row[0]
                db_vals = {
                    'mouth': row[1],
                    'front_eyes': row[2],
                    'back_eyes': row[3],
                    'tentacles': row[4],
                    'limbs': row[5]
                }
                count = 0
                for k in keys:
                    if k in item and item[k] == db_vals[k]:
                        count += 1
                if count >= 2:
                    races.add(race_name)

    return jsonify(sorted(list(races)))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
