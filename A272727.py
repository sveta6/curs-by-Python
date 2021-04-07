mas = [0]
n = int(input())
for i in range(n):
    count = 0
    for j in range(len(mas)):
        if mas[j] == mas[-j - 1]:
            count += 1
    mas.append(count)
for i in mas[:-1]:
    print(i)
