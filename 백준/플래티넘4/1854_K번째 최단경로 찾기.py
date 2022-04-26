import sys
import heapq

input = sys.stdin.readline

n,m,k = map(int,input().split())
road = [[] for _ in range(n+1)]
check = [[float('inf')]*k for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    road[a].append((b,c))
heap = []
heapq.heappush(heap,(0,1)) # count, last
check[1][0] = 0
while heap:
    time, last = heapq.heappop(heap)
    for go, cost in road[last]:
        if cost + time < check[go][k-1]:
            check[go][k-1] = cost + time
            check[go].sort()
            heapq.heappush(heap, (cost+time, go))

for i in range(1,n+1):
    if check[i][k-1] == float('inf'):
        print(-1)
    else:
        print(check[i][k-1])
