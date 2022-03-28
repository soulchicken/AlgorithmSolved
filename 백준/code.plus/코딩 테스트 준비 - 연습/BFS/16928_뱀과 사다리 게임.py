import sys
from collections import deque
input = sys.stdin.readline
counts = [100]*101
snake_ladder = [0]*101
min_count = 100
for _ in range(sum(map(int,input().split()))):
    a,b = map(int,input().split())
    snake_ladder[a] = b
que = deque()
que.append( (0,1) ) # count,index
while que:
    cnt,idx = que.pop()
    if idx > 100:
        idx = 100
    elif snake_ladder[idx] != 0:
        idx = snake_ladder[idx]

    if counts[idx] > cnt and min_count > cnt:
        counts[idx] = cnt
        if idx == 100:
            min_count = cnt
        for i in range(1,7):
            que.append((cnt+1,idx+i))
print(counts[-1])
