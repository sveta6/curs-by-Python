a = int(input())
names = [input() for i in range(a)]
c = int(input())
result = []
while 1:
    if len(names) > 0:
        result.append(names[0])
        names.pop(0)
        a -= 1
    else:
        break
    t = 1
    for i in range(a // c):
        result.append(names[((i + 1) * c) - t])
        names.pop(((i + 1) * c) - t)
        a -= 1
        t += 1
for i in range(len(result)):
    print(result[i])

