import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    li = [int(input()) for _ in range(n)]
    i = 0
    while 1:
        i += 1
        m = []
        for j in li:
            m.append(j % i)
        if len(m) == len(set(m)):
            print(i)
            break
