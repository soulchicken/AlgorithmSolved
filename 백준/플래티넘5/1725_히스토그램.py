from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
li = deque()
stack = deque()
for _ in range(n):
    li.append(int(input()))
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
