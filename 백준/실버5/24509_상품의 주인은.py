import sys
input =sys.stdin.readline

answer  = []
n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int,input().split())))

for j in range(1,5):
    index = 0
    max_num = 0
    for i in range(len(li)):
        if li[i][j] > max_num:
            max_num = li[i][j]
            index = i
        elif li[i][j] == max_num and li[index][0] > li[i][0]:
            index = i
    answer.append(li[index][0])
    li.pop(index)
for i in answer:
    print(i, end = ' ')
