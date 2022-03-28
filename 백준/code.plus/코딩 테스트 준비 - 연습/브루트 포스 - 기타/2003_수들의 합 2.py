import sys
input = sys.stdin.readline
N,M = map(int,input().split())
li = list(map(int,input().split()))
count = 0
for i in range(N):
    total = 0
    for j in range(i,N):
        total += li[j]
        if total == M:
            count += 1
            break
print(count)