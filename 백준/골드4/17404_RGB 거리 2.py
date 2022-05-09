import sys
import copy
input = sys.stdin.readline

n = int(input())
li1 = [list(map(int,input().split())) for _ in range(n)]
li2 = copy.deepcopy(li1)
li3 = copy.deepcopy(li1)

li1[-1][0] = 2000000
li2[-1][1] = 2000000
li3[-1][2] = 2000000

for i in range(n-1,1,-1):
    li1[i-1][0] += min(li1[i][2],li1[i][1])
    li1[i-1][1] += min(li1[i][0],li1[i][2])
    li1[i-1][2] += min(li1[i][0],li1[i][1])

    li2[i-1][0] += min(li2[i][2],li2[i][1])
    li2[i-1][1] += min(li2[i][0],li2[i][2])
    li2[i-1][2] += min(li2[i][0],li2[i][1])

    li3[i-1][0] += min(li3[i][2],li3[i][1])
    li3[i-1][1] += min(li3[i][0],li3[i][2])
    li3[i-1][2] += min(li3[i][0],li3[i][1])

min1 = li1[0][0] + min(li1[1][2],li1[1][1])
min2 = li2[0][1] + min(li2[1][0],li2[1][2])
min3 = li3[0][2] + min(li3[1][0],li3[1][1])

print(min(min1,min2,min3))
