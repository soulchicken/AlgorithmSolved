import heapq
N, L = map(int,input().split())
li = list(map(int,input().split()))
heap = []
answer = []
for i in range(N):
    heapq.heappush(heap,(li[i],i))
    while heap[0][1] < i-L+1:
        heapq.heappop(heap)
    answer.append(heap[0][0])
print(' '.join(map(str,answer)))
