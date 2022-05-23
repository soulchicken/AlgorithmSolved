import heapq
import sys
input = sys.stdin.readline

N, K = map(int,input().split())

li = [list(map(int,input().split())) for _ in range(N)]
bag = [int(input()) for _ in range(K)]
li.sort()
bag.sort()

total = 0
heap = []

for i in range(K):
    while li and bag[i] >= li[0][0]:
        _,v = heapq.heappop(li)
        heapq.heappush(heap,-v)

    if heap:
        total -= heapq.heappop(heap)

    elif not li:
        break

print(total)
