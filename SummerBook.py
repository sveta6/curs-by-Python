home_books = int(input())
school_books = int(input())
hbooks = []
for i in range(home_books):
    hbooks.append(input())
for j in range(school_books):
    a = input()
    if a in hbooks:
        print('YES')
    else:
        print('NO')