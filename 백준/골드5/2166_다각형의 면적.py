import sys
input = sys.stdin.readline

li = [list(map(int,input().split())) for _ in range(int(input()))]

li.append([li[0][0],li[0][1]])

answer = 0
for i in range(len(li) - 1):
    answer += (li[i][0]*li[i+1][1]) - (li[i+1][0]*li[i][1])
print(round(abs(answer)/2,1))
