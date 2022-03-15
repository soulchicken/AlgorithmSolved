import sys
from collections import deque
N,M = map(int,input().split())
li = [list(map(int,input())) for _ in range(N)]
crush_li = [[[float('inf')]*M for _ in range(N)] for _ in range(2)]
que = deque()
que.append((0,0,1,0))
move = ((1,0),(-1,0),(0,1),(0,-1))
final_count = -1
answer = float('inf')
while que:
    i,j,count,crush = que.popleft()
    if count < answer and 0 <= i and i < N and 0 <= j and j < M and count < crush_li[crush][i][j]:
        if li[i][j] == 1:
            crush += 1
        if crush < 2:
            crush_li[crush][i][j] = count
            if i == N-1 and j == M - 1:
                answer = count
            for x,y in move:
                que.append((i+x,j+y,count+1,crush))
if answer == float('inf'):
    print(-1)
else:
    print(answer)
