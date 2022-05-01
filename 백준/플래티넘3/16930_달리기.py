from collections import deque

N,M,K = map(int,input().split())
li = [list(input()) for _ in range(N)]
x1,y1,x2,y2 = map(int,input().split())
x1,y1,x2,y2 = x1-1, y1-1, x2-1, y2-1
que = deque()
que.append((x1,y1)) # i, j

check = [[-1] * M for _ in range(N)]
check[x1][y1] = 0
di,dj=(1,-1,0,0),(0,0,1,-1)



while que:
    i, j = que.popleft()
    if i == x2 and j == y2:
        break
    
    for d in range(4):
        for k in range(1,K+1):
            i2,j2 = i + di[d]*k, j + dj[d]*k
            if i2 < 0 or i2 >= N or j2 < 0 or j2 >= M or li[i2][j2] == '#':
                break
            if check[i2][j2] == -1:
                que.append((i2,j2))
                check[i2][j2] = check[i][j] + 1
            elif check[i2][j2] == check[i][j] + 1: continue
            else: break


if check[x2][y2] == float('inf'): print(-1)
else: print(check[x2][y2])
