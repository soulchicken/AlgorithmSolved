import sys
input = sys.stdin.readline
i = 0
while True :
    i += 1
    n = int(input())
    if n == 0: break
    li = [input().rstrip() for _ in range(n)]
    index = [2] * n
    for _ in range(n*2-1):
        a,b = input().split()
        index[int(a)-1] -= 1
    print(i, li[index.index(1)])
