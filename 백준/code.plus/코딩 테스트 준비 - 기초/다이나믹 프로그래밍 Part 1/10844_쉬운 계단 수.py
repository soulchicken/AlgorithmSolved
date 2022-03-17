from collections import deque
N = int(input())
li = [[0]*10 for _ in range(N)] # i,j = N번째 칸, 숫자
for i in range(1,10):
    li[0][i] = 1
for i in range(1,N):
    for j in range(10):
        if j < 9: li[i][j] += li[i-1][j+1]
        if j > 0: li[i][j] += li[i-1][j-1]
        li[i][j] %= 1000000000
print(sum(li[N-1]) % 1000000000)
