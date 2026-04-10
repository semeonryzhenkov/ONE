import sqlite3
import sys

if len(sys.argv) < 4:
    sys.exit(1)

db_file = sys.argv[1]
max_height = int(sys.argv[2])
min_danger = int(sys.argv[3])

conn = sqlite3.connect(db_file)
cur = conn.cursor()

query = """
SELECT t.type
FROM AlienTypes t
JOIN Dangers d ON t.id = d.type_id
WHERE t.height > ? AND d.danger >= ?
ORDER BY d.danger DESC
"""

cur.execute(query, (max_height, min_danger))
for row in cur.fetchall():
    print(row[0])

conn.close()
