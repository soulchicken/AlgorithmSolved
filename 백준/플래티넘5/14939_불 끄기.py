import copy
arr = [list(map(int,input().replace('O','0').replace('#','1'))) for _ in range(10)]
li = copy.deepcopy(arr)

move = ((0,0),(1,0),(-1,0),(0,1),(0,-1))

def check(i,j):
    if i < 10 and i >= 0 and j < 10 and j >= 0:
        return True
    return False

def convert(i,j):
    for di,dj in move:
        if check(i+di,j+dj):
            li[i+di][j+dj] = 1 - li[i+di][j+dj]

min_answer = 999
for a in range(1<<10):
    li = copy.deepcopy(arr)
    answer = 0
    for i in range(10):
        if a & (1<<i):
            answer += 1
            convert(0,i)

    for i in range(1,10):
        for j in range(10):
            if li[i-1][j] == 0:
                answer += 1
                convert(i,j)
    flag = True
    for i in range(10):
        if not li[-1][i]:
            flag = False
            break
    if flag:
        min_answer = min(min_answer, answer)

if min_answer == 999:
    print(-1)
else:
    print(min_answer)