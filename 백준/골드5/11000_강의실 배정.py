import sys
import heapq
li = sorted([tuple(map(int,sys.stdin.readline().split())) for _ in range(int(input()))])
count = []
for i in range(len(li)):
    if count and li[i][0] >= count[0]:heapq.heappop(count)
    heapq.heappush(count,li[i][1])
print(len(count))
