li = [list(map(int,input().split())) for _ in range(19)]
n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    for i in range(19):
        li[i][b] = 1 - li[i][b]
    for i in range(19):
        li[a][i] = 1 - li[a][i]
for i in range(19):
    for j in range(19):
        print(li[i][j],end =' ')
    print()