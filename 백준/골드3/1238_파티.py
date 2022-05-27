import sys
from collections import deque
input = sys.stdin.readline
n,m,x = map(int,input().split())
road = [[] for _ in range(n+1)]
road2 = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    road[b].append((a,c))
    road2[a].append((b,c))

que = deque()
que.append((x,0)) # last, cost
check = [float('inf')]*(n+1)
while que:
    last,cost = que.popleft()
    if cost < check[last]:
        check[last] = cost
        for a,b in road[last]:
            que.append((a,b+cost))

que.append((x,0))
check2 = [float('inf')]*(n+1)

while que:
    last,cost = que.popleft()
    if cost < check2[last]:
        check2[last] = cost
        for a,b in road2[last]:
            que.append((a,b+cost))

answer = []
for i in range(1,n+1):
    answer.append(check[i]+check2[i])
print(max(answer))
