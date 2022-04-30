import sys
import math
input = sys.stdin.readline
n = int(input())
li = list(map(int,input().split()))
B,C = map(int,input().split())
count = 0
for i in range(n):
    li[i] -= B
    count += 1
    if li[i] > 0 :
        count += math.ceil(li[i] / C)
print(count)
