lst = ['A', 'B','C', 'A', 'C', 'A', 'B', 'A', 'A']

map = {}
for c in lst:
    if(c in map):
        map[c] += 1
    else:
        map[c] = 1

for e, i in map.items():
    print(e, i) 