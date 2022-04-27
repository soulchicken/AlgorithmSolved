import sys
import heapq
input = sys.stdin.readline
N,E = map(int,input().split())
road = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    road[a].append((b,c))
    road[b].append((a,c))
u,v = map(int,input().split())
check = [[float('inf')]*(N+1) for _ in range(3)] # 1,u,v 출발
index_list = [1,u,v]
for i in range(3):
    heap = []
    index = index_list[i]
    heapq.heappush(heap,(0,index,0))# count,last,time
    while heap:
        count,last,index = heapq.heappop(heap)
        if check[i][last] > count:
            check[i][last] = count
            for to_go, cost in road[last]:
                heapq.heappush(heap,(count + cost, to_go, index))

count_uv = check[0][u] + check[1][v] + check[2][N]
count_vu = check[0][v] + check[2][u] + check[1][N]
count_1N = min(count_uv,count_vu)
print(count_1N if count_1N != float('inf') else -1)
