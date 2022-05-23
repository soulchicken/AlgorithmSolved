import heapq

V, E = map(int,input().split())
route = [[] for _ in range(V+1)]

for _ in range(E):
    a,b,c = map(int,input().split())
    route[a].append((c,b))
    route[b].append((c,a))

check = [True]*(V+1)
heap = [(0,1)] # cost, last

answer = 0
i = 0
while i != V:
    cost, last = heapq.heappop(heap)
    if check[last]:
        check[last] = False
        answer += cost
        i += 1
        for li in route[last]:
            heapq.heappush(heap,li)
print(answer)
