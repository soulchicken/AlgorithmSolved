N, K = map(int,input().split())
li = [[0]*(N+1) for _ in range(K)]
for i in range(N+1):
    li[0][i] = 1

for i in range(K):
    li[i][0] = 1

for i in range(1,K):
    for j in range(1,N+1):
        li[i][j] = (li[i-1][j] + li[i][j-1]) % 1000000000

print(li[K-1][N])
