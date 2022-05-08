from collections import deque

N,M = map(int,input().split())
Hx,Hy = map(int,input().split())
Ex,Ey = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(N)]

move = ((0,1),(0,-1),(1,0),(-1,0))

check = [[[float('inf')]*M for _ in range(N)] for _ in range(2)]
# flag, i,j 에 count가 들어가는 구조

que = deque([(0,Hx-1,Hy-1,1)]) # count, i, j,flag(1은 아직 벽안뚫)
num = float('inf')
while que:
    count, i,j,flag = que.popleft()
    if i == Ex-1 and j == Ey-1:
        num = count
        break
    if 0 <= i < N and 0 <= j < M:
        if li[i][j] and not flag:
            continue
        elif li[i][j] and flag:
            flag = 0

        if check[flag][i][j] > count:
            check[flag][i][j] = count
            for di,dj in move:
                que.append((count+1,i+di,j+dj,flag))


if num == float('inf'):print(-1)
else:print(num)
