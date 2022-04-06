import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
want_start, want_go = map(int,input().split())
m = int(input())
li = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    li[a].append(b)
    li[b].append(a)

que = deque()
que.append((want_start,want_start,0)) # start, end, count

check = [float('inf')] * (n+1)
while que:
    start, end, count = que.popleft()
    if count < check[end]:
        check[end] = count
        for i in li[end]:
            que.append((end, i, count + 1))
if check[want_go] == float('inf'): print(-1)
else: print(check[want_go])