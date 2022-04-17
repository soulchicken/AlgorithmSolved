import sys
import heapq
input = sys.stdin.readline
n = int(input())
total = 0
heap = []
for _ in range(n):
    heapq.heappush(heap,int(input()))
while len(heap) != 1:
    k = heapq.heappop(heap) + heapq.heappop(heap)
    heapq.heappush(heap,k)
    total += k
print(total)
