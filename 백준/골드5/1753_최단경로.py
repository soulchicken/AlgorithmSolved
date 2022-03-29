import sys
import heapq
input = sys.stdin.readline
V, E = map(int,input().split())
start = int(input())
check = [True] * (V+1)
road = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    road[u].append((v,w))
time = [float('inf')] * (V + 1)
heap = []
heapq.heappush(heap, (0,start,start) ) # time, start, end
while heap:
    t, start, end = heapq.heappop(heap)
    if time[end] > t:
        time[end] = t
        for v,w in road[end]:
            heapq.heappush(heap, (t+w, end, v) )
            
for i in range(1,V+1):
    if time[i] == float('inf'): print('INF')
    else: print(time[i])
