s = input()
flag = None
count = 0
t = 1
for i in range(len(s)):
    if flag != s[i]:
        count = 0
        flag = s[i]
    else:
        count = 1
       
    if flag == 'c':
        t *= (26 - count)
    else:
        t *= (10 - count)
print(t)
