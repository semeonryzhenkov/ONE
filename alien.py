import sqlite3

c = sqlite3.connect('aliens.db')
d = c.cursor()

s = '''
SELECT a.subject, t.type, a.grasping, a.moving, t.height, d.danger
FROM Aliens a
JOIN AlienTypes t ON a.type_id = t.id
JOIN Dangers d ON t.id = d.type_id
'''

d.execute(s)
r = d.fetchall()

for x in r:
    print(f"{x[0]};{x[1]};{x[2]};{x[3]};{x[4]};{x[5]}")

d.close()
c.close()
