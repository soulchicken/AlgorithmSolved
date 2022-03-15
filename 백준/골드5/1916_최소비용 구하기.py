import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
city = [float('inf')]*(N+1)
route = [[] for _ in range(N+1)]

for _ in range(M):
    start_route,end_route,money = map(int,input().split())
    route[start_route].append((end_route,money))
    
start, end  = map(int,input().split())
heap = []
heapq.heappush(heap,(0,start,start))

while heap:
    count, last, go = heapq.heappop(heap)
    if city[go] > count:
        city[go] = count
        for n,m in route[go]:
            heapq.heappush(heap, (count+m,go,n))
print(city[end])
