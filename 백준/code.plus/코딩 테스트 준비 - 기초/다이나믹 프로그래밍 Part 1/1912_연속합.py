import sys
n = int(input())
li = list(map(int,input().split()))
for i in range(1,len(li)):
    if li[i-1] > 0:
        li[i] += li[i-1]
print(max(li))