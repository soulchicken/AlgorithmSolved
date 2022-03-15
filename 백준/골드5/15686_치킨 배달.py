import sys
from itertools import combinations as com
input = sys.stdin.readline
N, M = map(int,input().split())
chick = []
home = []
for i in range(N):
    li = list(map(int,input().split()))
    for j in range(N):
        if li[j] == 1:
            home.append((i,j))
        elif li[j] == 2:
            chick.append((i,j))

min_num = 3000
for pick in com(chick,M):
    num = 0

    for i,j in home:
        pick_num = 3000

        for x,y in pick:
            pick_num = min(abs(i-x)+abs(j-y),pick_num)
            
        num += pick_num

    min_num = min(num,min_num)
print(min_num)
