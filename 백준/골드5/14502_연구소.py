from collections import deque
import copy
N,M = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(N)]
MAX = 0
move = ((0,1),(1,0),(-1,0),(0,-1))
def check(arr):
    que = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                for x,y in move:
                    que.append((i+x,j+y))
    while que:
        a,b = que.popleft()
        if 0 <= a < N and 0 <= b < M and arr[a][b] == 0:
            arr[a][b] = 2
            for x,y in move:
                que.append((a+x,b+y))

    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                count += 1
    return count

ans = 0
for a in range(N):
    for b in range(M):
        if li[a][b] == 0:
            li[a][b] = 1
        else:
            continue
        for c in range(N):
            for d in range(M):
                if li[c][d] == 0:
                    li[c][d] = 1
                else:
                    continue
                for e in range(N):
                    for f in range(M):
                        if li[e][f] == 0:
                            li[e][f] = 1
                            ans = max(ans,check(copy.deepcopy(li)))
                            li[e][f] = 0
                li[c][d] = 0
        li[a][b] = 0
print(ans)
