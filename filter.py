for _ in range(int(input())):
    txt = input()
    if '%' in txt:
        print(txt.replace('%',''))
    elif '####' not in txt:
        print(txt)