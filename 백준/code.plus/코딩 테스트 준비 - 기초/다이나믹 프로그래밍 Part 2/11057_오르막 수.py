n = int(input())
li = [[1]*10 for _ in range(n)]

for i in range(1,n):
    for j in range(1,10):
        li[i][j] = (li[i-1][j] + li[i][j-1]) % 10007
print(sum(li[-1]) % 10007)
