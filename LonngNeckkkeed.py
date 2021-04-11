s = input().upper()
k = 0
for i in range(len(s)):
    if s.count(s[i]) > k:
        k = s.count(s[i])
print(k)