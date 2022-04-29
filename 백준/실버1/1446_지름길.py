import sys
import heapq
input = sys.stdin.readline
N,D = map(int,input().split())
li = [[] for _ in range(10001)]
heap = []
for _ in range(N):
    a,b,c = map(int,input().split())
    li[a].append((b,c))
heap = []# cost, last
heapq.heappush(heap,(0,0))
while heap:
    time, last = heapq.heappop(heap)
    if last > D:
        continue
    if last == D:
        print(time)
        break
    heapq.heappush(heap,(time+1, last + 1))
    for l,t in li[last]:
        heapq.heappush(heap, (t+time, l))
