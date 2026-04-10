import requests

d = requests.get("http://127.0.0.1:8080").json()

m = 0
i = 0
for x in range(len(d)):
    y = abs(d[x]["a"] - d[x]["b"])
    if y > m:
        m = y
        i = x + 1

s = set()
c = 0
for x in d:
    a = x["a"]
    b = x["b"]
    if a > 49:
        s.add(a)
    if b > 49:
        s.add(b)
    if a < 49 and b < 49:
        c += 1

print(i)
print(*sorted(s))
print(c)
