import sys
input = sys.stdin.readline
n,m = map(int,input().split())
flag = True
for _ in range(m):
    input()
    stack = list(map(int,input().split()))
    if flag and stack != sorted(stack,reverse = True):
        flag = False
if flag: print('Yes')
else: print('No')
