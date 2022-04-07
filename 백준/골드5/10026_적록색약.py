import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
RGB = [list(input()) for _ in range(n)]
check = [[0]*n for _ in range(n)]
move = ((0,1),(0,-1),(1,0),(-1,0))
RGB_count = 0
RB_count = 0

que = deque()

def check_index(i,j):
    if 0 <= i and i < n and 0 <= j and j < n:
        return True
    return False

def RGB_BFS(color):
    while que:
        i,j = que.popleft()
        if not check_index(i,j):
            continue
        elif check[i][j] == 1 or color != RGB[i][j]:
            continue
        else:
            check[i][j] = 1
            for x,y in move:
                que.append((i+x,j+y))
                
def RB_BFS(color):
    while que:
        i,j = que.popleft()
        if not check_index(i,j):
            continue
        elif check[i][j] == 1:
            continue
        elif color in ['R', 'G'] and RGB[i][j] not in ['R','G']:
            continue
        elif color == 'B' and RGB[i][j] != 'B':
            continue
        else:
            check[i][j] = 1
            for x,y in move:
                que.append((i+x,j+y))
            
count = 0
for i in range(n):
    for j in range(n):
        if check[i][j] == 0:
            count += 1
            color = RGB[i][j]
            que.append((i,j))
            RGB_BFS(color)

check = [[0]*n for _ in range(n)]

print(count,end =' ')
count = 0
for i in range(n):
    for j in range(n):
        if check[i][j] == 0:
            count += 1
            color = RGB[i][j]
            que.append((i,j))
            RB_BFS(color)

print(count)
