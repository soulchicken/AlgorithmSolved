import sys
input = sys.stdin.readline
n = int(input())
li = [int(input()) for _ in range(n)]
li.sort(reverse = True)
stack = []
stack.append(li.pop())
while len(stack) != stack[-1] + 1:
    stack.append(li.pop())
print(len(stack))
