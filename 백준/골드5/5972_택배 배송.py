import sys
import heapq
input = sys.stdin.readline

N,M = map(int,input().split())
road = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    road[a].append((b,c))
    road[b].append((a,c))
heap = []
heapq.heappush(heap,(0,1)) # count, last
check = [float('inf')] * (N+1)
while heap:
    count, last = heapq.heappop(heap)
    if check[last] > count:
        check[last] = count
        for to_go, cost in road[last]:
            heapq.heappush(heap,(count + cost, to_go))
print(check[-1])
