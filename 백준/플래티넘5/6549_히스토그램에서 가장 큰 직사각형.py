from collections import deque
import sys
input = sys.stdin.readline

while 1:
    li = deque(map(int,input().split()))
    n = li.popleft()
    
    if n == 0:
        break
    stack = deque()
    ans = 0 
    for i in range(n):
        while stack and li[stack[-1]] > li[i]:
            x = stack.pop()
            if not stack:
                ans = max(ans, i * li[x])
            else:
                ans = max(ans, (i - stack[-1] - 1) * li[x])
        stack.append(i)
    while stack:
        x = stack.pop()

        if not stack:
            ans = max(ans,n * li[x])
        else:
            ans = max(ans,(n - stack[-1] - 1)*li[x])
    print(ans)
