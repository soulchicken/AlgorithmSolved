import sys
import heapq
input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    for i in list(map(int,input().split())):
        heapq.heappush(heap,i)
        if len(heap) > n:
            heapq.heappop(heap)
print(heapq.heappop(heap))
