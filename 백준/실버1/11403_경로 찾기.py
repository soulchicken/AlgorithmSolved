import sys
input = sys.stdin.readline

n = int(input())

route = [list(map(int,input().split())) for _ in range(n)]

for link in range(n):
    for i in range(n):
        for j in range(n):
            if route[i][j] == 1 or route[i][link] + route[link][j] == 2:
                route[i][j] = 1

for c in route:
    for i in c:
        print(i, end= ' ')
    print()
