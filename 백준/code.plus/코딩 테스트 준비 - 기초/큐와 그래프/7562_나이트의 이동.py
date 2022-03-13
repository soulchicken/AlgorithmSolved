import sys
from collections import deque
input = sys.stdin.readline
move = ((1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1),(-1,-2),(-2,-1))
for _ in range(int(input())):
    max_num = float('inf')
    que = deque()
    n = int(input())
    li = [[float('inf')]*n for _ in range(n)]
    a,b = map(int,input().split())
    x,y = map(int,input().split())
    que.append((a,b,0)) # i,j, count
    while que:
        i,j,count = que.popleft()
        if 0 <= i and i < n and 0 <= j and j < n and li[i][j] > count and max_num > count:
            li[i][j] = count
            if i == x and j == y:
                max_num = count
            for di,dj in move:
                que.append((i+di,j+dj,count+1))
    print(max_num)