import sys
input = sys.stdin.readline
n = int(input())
li = [int(input()) for _ in range(n)]
li.sort()
total = 0
for i in range(n):
    if li[i] * (n-i) >= total:
        total = li[i] * (n-i)
print(total)
