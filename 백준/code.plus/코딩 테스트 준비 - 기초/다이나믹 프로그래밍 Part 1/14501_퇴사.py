import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
li = [-1]*21
que = deque()
que.append((1,0))
T = [0]*21
P = [0]*21
for i in range(1,n+1):
    t,p = map(int,input().split())
    T[i] = t
    P[i] = p
T[0] = 1

while que:
    index, pay = que.popleft()
    if index < n+2 and li[index] < pay:
        li[index] = pay
        que.append((index + T[index], pay + P[index]))
        que.append((index + 1, pay))

print(li[n+1])
