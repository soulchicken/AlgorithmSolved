import sys
from collections import deque
input = sys.stdin.readline
stack = list(input().rstrip())
queue = deque()
for _ in range(int(input())):
    s = input().rstrip()
    if s == "L" and stack:
        queue.appendleft(stack.pop())
    elif s == "D" and queue:
        stack.append(queue.popleft())
    elif s == "B" and stack:
        stack.pop()
    elif s[0] == "P":
        a, b = s.split()
        stack.append(b)

answer = ""
for i in stack:
    answer += i
for i in queue:
    answer += i
print(answer)
