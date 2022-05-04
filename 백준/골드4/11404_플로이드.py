import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

cost = [[float('inf')]*n for _ in range(n)]

for i in range(n):
    cost[i][i] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    cost[a-1][b-1] = min(cost[a-1][b-1],c)

for link in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j],cost[i][link] + cost[link][j])

for c in cost:
    for i in c:
        if i == float('inf'): print(0,end= ' ')
        else: print(i, end= ' ')
    print()
