#!/usr/bin/env python3

# Читаем траекторию из файла
with open('path.txt', 'r') as f:
    trajectory = f.read().strip()

max_len = 0
max_start = -1

i = 0
while i < len(trajectory):
    if trajectory[i] == 'U':
        # Начало последовательности U
        start = i
        length = 0
        while i < len(trajectory) and trajectory[i] == 'U':
            length += 1
            i += 1
        
        # Проверяем, является ли эта последовательность максимальной
        if length > max_len:
            max_len = length
            max_start = start
    else:
        i += 1

print(max_start)
