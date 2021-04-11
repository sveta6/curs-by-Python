n = int(input())
coord = []
table = [[el for el in input().split(',')] for i in range(n)]
m = int(input())
for _ in range(m):
    coord = input().split(',')
    x = int(coord[0])
    y = int(coord[1])
    j = table[x][y]
    if ',' in table[x][y]:
        j = table[x][y]
        a = j[:j.find(',')]
        b = j[j.find(',') + 2:]
        print(','.join([a, b]))
    elif '\n' in table[x][y]:
        i = table[x][y]
        a = i[:i.find('\n')]
        b = i[i.find('\n') + 2:]
        print('\n'.join([a, b]))
    else:
        print(table[x][y])