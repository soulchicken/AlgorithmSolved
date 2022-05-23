import heapq
n = int(input())
star = [list(map(float,input().split())) for _ in range(n)]
route = [[] for _ in range(n)]

for i in range(n):
    for j in range(i+1,n):
        cost = ((star[i][0] - star[j][0])**2 + (star[i][1] - star[j][1])**2)**0.5
        route[i].append((cost,j))
        route[j].append((cost,i))

check = [True]*n
heap = [(0,0)]

answer = 0
i = 0
while i != n:
    cost, last = heapq.heappop(heap)
    if check[last]:
        check[last] = False
        answer += cost
        i += 1
        for li in route[last]:
            heapq.heappush(heap,li)
print(answer)
