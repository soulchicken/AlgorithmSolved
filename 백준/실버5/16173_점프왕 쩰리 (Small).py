from collections import deque
n = int(input())
check = [[1]*n for _ in range(n)]

li = [list(map(int,input().split())) for _ in range(n)]

que = deque()
que.append((0,0))

while que:
    i,j = que.popleft()
    if 0 <= i < n and 0 <= j < n and check[i][j]:
        check[i][j] = 0
        a = li[i][j]
        que.append((i+a,j))
        que.append((i,j+a))
print(['HaruHaru','Hing'][check[-1][-1]])
