import sys
input = sys.stdin.readline
for _ in range(int(input())):
    flag = True
    n = int(input())
    li = [input().strip() for _ in range(n)]
    li.sort()
    for i in range(n-1):
        a = li[i]
        b = li[i+1]
        if len(a) > len(b):
            a,b = li[i+1], li[i]

        if a == b[:len(a)]:
            flag = False
            break

    if flag:
        print('YES')
    else:
        print('NO')
