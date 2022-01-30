h, w = map(int,input().split())
li = [[0 for _ in range(w)] for _ in range(h)]
for _ in range(int(input())):
    l, d, x, y = map(int,input().split())
    x -= 1
    y -= 1

    if d == 0:
        for i in range(l):
            li[x][y+i] = 1
    else:
        for i in range(l):
            li[x+i][y] = 1

for i in range(h):
    for j in range(w):
        print(li[i][j],end =' ')
    print()