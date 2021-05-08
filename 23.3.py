line = input().lower()
lines = line.split()
lst = [sum(x in 'уеыаоэяию' for x in lin) for lin in lines]
result =("Пам парам", "Парам пам-пам")[len(set(lst)) == 1]
print(result)