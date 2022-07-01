from collections import deque
li = deque([i+1 for i in range(int(input()))])
stack = []

while li:
    stack.append(li.popleft())
    if li:
        li.append(li.popleft())

print(*stack)
