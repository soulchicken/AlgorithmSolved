import sys
from collections import deque
input = sys.stdin.readline
n,m,v = map(int,input().split())
li = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    li[a].append(b)
    li[b].append(a)
for i in li:
    i = i.sort()
li_dfs = [False]*(n+1)
def DFS(n):
    if li_dfs[n] == True:
        return
    li_dfs[n] = True
    print(n,end=' ')
    for i in li[n]:
        DFS(i)
DFS(v)
print()
# BFS
li_bfs = [False]*(n+1)
queue = deque()
queue.append(v)
def BFS(n):
    if li_bfs[n] == True:
        return
    li_bfs[n] = True
    print(n,end=' ')
    queue.extend(li[n])

while queue:
    BFS(queue.popleft())