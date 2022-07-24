n = int(input())
flag = False
while 1:
    if n == 1:
        flag = True
    if n % 2 == 1:
        break
    n //= 2
if flag: print(1)
else: print(0)
