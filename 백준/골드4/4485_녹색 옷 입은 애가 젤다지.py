import sys
import heapq
input = sys.stdin.readline
k = 0
move = ((0,1),(0,-1),(1,0),(-1,0))

def check_index(i,j,n):
    if i >= 0 and i < n and j >= 0 and j < n:
        return True
    return False

while 1:
    n = int(input())
    if n == 0: break
    k += 1
    heap = []
    road = [list(map(int,input().split())) for _ in range(n)]
    dp = [[float('inf')]*n for _ in range(n)]
    heapq.heappush(heap,(0,0,road[0][0])) # i,j,total
    while heap:
        i,j,total = heapq.heappop(heap)
        if dp[i][j] > total:
            dp[i][j] = total
            for di,dj in move:
                x,y = i + di, j + dj
                if check_index(x,y,n):
                    heapq.heappush(heap,(x,y,total + road[x][y]))
    print(f'Problem {k}: {dp[-1][-1]}')
