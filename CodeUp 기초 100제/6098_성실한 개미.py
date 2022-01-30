li = [list(map(int,input().split())) for _ in range(10)]
antX = 1
antY = 1
while True:
    if li[antY][antX+1] == 1 and li[antY+1][antX] == 1:
        li[antY][antX] = 9
        break
    elif li[antY][antX+1] == 2:
        li[antY][antX] = 9
        li[antY][antX+1] = 9
        break
    elif li[antY][antX+1] == 0:
        li[antY][antX] = 9
        antX += 1
    elif li[antY+1][antX] == 2:
        li[antY][antX] = 9
        li[antY+1][antX] = 9
        break
    elif li[antY+1][antX] == 0:
        li[antY][antX] = 9
        antY += 1
for i in range(10):
    for j in range(10):
        print(li[i][j],end =' ')
    print()