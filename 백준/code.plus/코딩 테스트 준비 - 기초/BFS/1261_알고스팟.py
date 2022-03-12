import sys
from collections import deque
M,N = map(int,input().split())
rooms = [list(map(int,input().strip())) for _ in range(N)]
counts = [[10000]*(M+2) for _ in range(N+2)]

counts[1][1] = 0
for _ in range(M+N):
    for i in range(1,N+1):
        for j in range(1,M+1):
            n = rooms[i-1][j-1]
            counts[i][j] = min(counts[i][j],counts[i+1][j]+n,counts[i-1][j]+n,counts[i][j+1]+n,counts[i][j-1]+n)
print(counts[-2][-2])