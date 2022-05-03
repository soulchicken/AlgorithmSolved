import copy
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
li = copy.deepcopy(arr)

move = ((0,0),(1,0),(-1,0),(0,1),(0,-1))

def check(i,j):
    if i < N and i >= 0 and j < N and j >= 0:
        return True
    return False

def convert(i,j):
    for di,dj in move:
        if check(i+di,j+dj):
            li[i+di][j+dj] = 1 - li[i+di][j+dj]

min_answer = float('inf')
for a in range(1<<N):
    li = copy.deepcopy(arr)
    answer = 0
    for i in range(N):
        if a & (1<<i):
            answer += 1
            convert(0,i)

    for i in range(1,N):
        for j in range(N):
            if li[i-1][j] == 1:
                answer += 1
                convert(i,j)
    flag = True
    for i in range(N):
        if li[-1][i]:
            flag = False
            break
    if flag:
        min_answer = min(min_answer, answer)

if min_answer == float('inf'):
    print(-1)
else:
    print(min_answer)
