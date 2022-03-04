import sys
input = sys.stdin.readline
n,m = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(n)]
check = [[True] * m for _ in range(n)]
count = [0]
move = [(1,0),(-1,0),(0,-1),(0,1)]
stack = []
def DFS(i,j,depth, total):
    if depth == 4:
        if count[0] < total:
            count[0] = total
        return
    check[i][j] = False
    for di,dj in move:
        if di+i > -1 and di+i < n and dj+j > -1 and dj+j < m and check[di+i][dj+j]:
            DFS(di+i,dj+j,depth+1,total+li[di+i][dj+j])
    check[i][j] = True

for i in range(n):
    for j in range(m):
        stack.append((i,j))
        DFS(i,j,1,li[i][j])
for i in range(n-2):
    for j in range(m-1):
        count[0] = max(count[0],li[i][j+1]+li[i+1][j+1]+li[i+2][j+1]+li[i+1][j],
        li[i][j]+li[i+1][j]+li[i+2][j]+li[i+1][j+1])

for i in range(n-1):
    for j in range(m-2):
        count[0] = max(count[0],li[i+1][j]+li[i+1][j+1]+li[i+1][j+2]+li[i][j+1],
        li[i][j]+li[i][j+1]+li[i][j+2]+li[i+1][j+1])
print(count[0])
