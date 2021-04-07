n = int(input())
list = ['']*n
for i in range(n):
    list[i] = input()
k = int(input())
for i in range(k):
    x = int(input())
    tmp = ['']*x
    for j in range(x):
        tmp[j] = list[int(input())-1]
    list = tmp
for i in range(len(list)):
    print(list[i])