import sys
from collections import deque
input = sys.stdin.readline

N,M,K,X = map(int,input().split())
length = [float('inf')]*(N+1)
way = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    way[a].append(b)
que = deque()
que.append((X,0)) # visit, count
while que:
    visit, count = que.popleft()
    if length[visit] > count:
        length[visit] = count
        for i in range(len(way[visit])):
            que.append((way[visit][i], count+1))
cities = []
for i in range(N+1):
    if length[i] == K:
        cities.append(i)
if cities:
    for i in cities:
        print(i)
else:
    print(-1)
