import sys
input = sys.stdin.readline
N = int(input())
me = int(input())
li = [int(input()) for _ in range(N-1)]
count = 0
li.sort()
while 1:
    if N == 1 or li[-1] < me:
        break
    li[-1] -= 1
    me += 1
    count += 1
    li.sort()
print(count)
