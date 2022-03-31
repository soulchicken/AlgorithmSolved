import sys
input = sys.stdin.readline
n = int(input())
li = [int(input()) for _ in range(n)]
if n <= 2:
    print(sum(li))
else:
    no_step = [0]*n
    step = [0]*n
    step2 = [0]*n
    no_step[1] = li[0]
    step[0] = li[0]
    step[1] = li[1]
    step2[0] = li[0]
    step2[1] = li[0] + li[1]
    for i in range(2,n):
        no_step[i] = max(step[i-1],step2[i-1])
        step[i] = no_step[i-1] + li[i]
        step2[i] = step[i-1] + li[i]
    print(max(step[-1],step2[-1]))
