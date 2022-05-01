import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
li = sorted(list(map(int,input().split())))[::-1]
M = int(input())
box = sorted(list(map(int,input().split())))[::-1]
m = M
count = 0
flag = True
while box:
    if not li:
        flag = False
        break
    count += 1
    i = 0
    while i < len(li):
        in_flag = False
        for j in range(len(box)):
            if li[i] >= box[j]:
                box.pop(j)
                in_flag = True
                break
        if in_flag:
            i += 1
        else:
            li.pop(i)
    if m == len(box):
        flag = False
        break
        
if flag : print(count)
else: print(-1)
