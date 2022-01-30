n = int(input())
li = [[0 for _ in range(19)] for _ in range(19)]
for _ in range(n):
    a, b = map(int,input().split())
    li[a-1][b-1] = 1

for i in range(19):
    for j in range(19):
        print(li[i][j],end =' ')
    print()