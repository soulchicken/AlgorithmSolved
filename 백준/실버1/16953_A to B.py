from collections import deque
A,B = map(int,input().split())
que = deque()
que.append((A,1))
answer = float('inf')
while que:
    a,count = que.popleft()
    if a == B:
        answer = count
        break
    elif a > B:
        continue
    que.append( (a*2,count+1) )
    que.append( (a*10+1,count+1) )
if answer == float('inf'):
    print(-1)
else:
    print(answer)
