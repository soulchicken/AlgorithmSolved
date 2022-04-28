import sys
import heapq
input = sys.stdin.readline

N, T = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(N)]
heap = []
heapq.heappush(heap,(T,1,0,1)) # time,count, i, j
heapq.heappush(heap,(T,1,1,0))
def check(i,j):
    if i >= 0 and i < N and j >= 0 and j < N:
        return True
    return False
move = ((0,1),(1,0),(0,-1),(-1,0))
dp = [[[float('inf')]*N for _ in range(N)] for _ in range(3)]
while heap:
    time, count, i, j = heapq.heappop(heap)
    if not check(i,j):
        continue
    if count % 3 == 0:
        time += li[i][j]

    if dp[count % 3][i][j] > time:
        dp[count % 3][i][j] = time
        for x,y in move:
            heapq.heappush(heap,(time+T, count + 1, i+x,j+y))
print(min(dp[0][-1][-1],dp[1][-1][-1],dp[2][-1][-1]))
