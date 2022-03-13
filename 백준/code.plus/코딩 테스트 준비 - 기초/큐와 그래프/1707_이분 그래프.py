import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    v,e = map(int,input().split())
    li = [[] for _ in range(v+1)]
    flag = True
    check = [None]*(v+1)
    visited = [True]*(v+1)
    que = deque()

    for _ in range(e):
        a,b = map(int,input().split())
        li[a].append(b)
        li[b].append(a)

    for num in range(v+1):
        if visited[num]:
            check[num] = True
            visited[num] = False
            for n in li[num]:
                que.append((num,n))
        while que:
            if not flag:
                break
            start, end = que.popleft()
            if check[start] == check[end]:
                flag = False
                
            elif check[end] == None:
                if check[start]: check[end] = False
                else: check[end] = True
                
            if visited[end]:
                visited[end] = False
                for n in li[end]:
                    que.append((end,n))
    
    
    if flag:
        print('YES')
    else:
        print('NO')