with open('path.txt') as f:
    s = f.read().strip()

max_len = 0
max_idx = 0
cur_len = 0

for i, c in enumerate(s):
    if c == 'U':
        cur_len += 1
    else:
        if cur_len > max_len:
            max_len = cur_len
            max_idx = i - cur_len
        cur_len = 0

if cur_len > max_len:
    max_idx = len(s) - cur_len

print(max_idx)
