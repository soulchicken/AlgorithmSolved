import sys
input = sys.stdin.readline

for _ in range(int(input())):
    num = int(input())
    flag = False
    for i in range(2,65):
        x = []
        n = num
        while n != 0:
            x.append(n % i)
            n //= i
        if x == x[::-1]:
            flag = True
            break
    if flag: print(1)
    else: print(0)
