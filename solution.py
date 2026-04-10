import sqlite3
import sys

if len(sys.argv) < 4:
    sys.exit(1)

f = sys.argv[1]
h = int(sys.argv[2])
d = int(sys.argv[3])

con = sqlite3.connect(f)
cur = con.cursor()

sql = """
SELECT DISTINCT t.type
FROM AlienTypes t
JOIN Dangers d ON t.id = d.type_id
WHERE t.height > ? AND d.danger >= ?
ORDER BY d.danger DESC
"""

cur.execute(sql, (h, d))
for r in cur.fetchall():
    print(r[0])

con.close()
