import heapq
import sys
input = sys.stdin.readline
heap1 = [] # 높은게  앞에 오도록
heap2 = [] # 낮은게 앞에 오도록
for i in range(int(input())):
    n = int(input())
    if len(heap1) == len(heap2):
        heapq.heappush(heap1,-n)
    else: heapq.heappush(heap2,n)
    if heap2 and -heap1[0] > heap2[0]:
        a = -heapq.heappop(heap1)
        b = heapq.heappop(heap2)
        heapq.heappush(heap1,-b)
        heapq.heappush(heap2,a)
    print(-heap1[0])
