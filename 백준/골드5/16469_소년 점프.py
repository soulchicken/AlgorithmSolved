from collections import deque
C,R = map(int,input().split())
li = [list(map(int,list(input()))) for _ in range(C)]
nsc_start = [list(map(int,input().split())) for _ in range(3)]
INF = 10001
nsc_check = [[[INF]*R for _ in range(C)] for _ in range(3)] # 넉살 스윙스 창모

move = ((0,1),(0,-1),(1,0),(-1,0))

for man in range(3):
    que = deque() # count,i,j
    que.append((0,nsc_start[man][0]-1,nsc_start[man][1]-1))
    while que:
        count, i,j = que.popleft()
        if 0 <= i < C and 0 <= j < R and li[i][j] == 0 and nsc_check[man][i][j] > count:
            nsc_check[man][i][j] = count
            for di,dj in move:
                que.append((count+1,i+di,j+dj))

table = [[INF]*R for _ in range(C)]
ans = INF
count = 0

for i in range(C):
    for j in range(R):
        table[i][j] = max(nsc_check[0][i][j],nsc_check[1][i][j],nsc_check[2][i][j])
        if ans > table[i][j]:
            ans = table[i][j]
            count = 1
        elif ans == table[i][j]:
            count += 1

if ans != INF:
    print(ans)
    print(count)
else:
    print(-1)
