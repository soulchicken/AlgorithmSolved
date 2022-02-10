s = input()
i = 0
flag = 'YES'
length = len(s)
while i != length:
    if i+1 <= length and s[i:i+2] == 'pi' or s[i:i+2] == 'ka':
        i += 2
        continue
    elif i + 2 <= length and s[i:i+3] == 'chu':
        i += 3
        continue
    flag = 'NO'
    break
print(flag)