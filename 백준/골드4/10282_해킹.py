import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    n,d,c = map(int,input().split())
    check = [float('inf')]*(n+1)
    route = [[] for _ in range(n+1)]
    for _ in range(d):
        a,b,s = map(int,input().split())
        route[b].append((a,s))
    que = deque()
    que.append((c,0))
    while que:
        last, time = que.popleft()
        if time < check[last]:
            check[last] = time
            for x,y in route[last]:
                que.append((x,y+time))
    MAX = 0
    count = 0
    for i in range(len(check)):
        if check[i] != float('inf'):
            count += 1
            MAX = max(MAX, check[i])

    print(count,MAX)
