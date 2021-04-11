import re
t = input()
key = 'text'
print(re.search(f'\?.*?{key}=(.*)[&\n]', t)[1])