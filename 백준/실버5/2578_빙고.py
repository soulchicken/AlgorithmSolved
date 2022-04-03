bingo_X = []
bingo_Y = [[0]*5 for _ in range(5)]
x = []
y = []
for i in range(5):
    li = list(map(int,input().split()))
    x.append(li[i])
    y.append(li[5-1-i])
    bingo_X.append(li)
for i in range(5):
    for j in range(5):
        bingo_Y[i][j] = bingo_X[j][i]

speak = []
for _ in range(5):
    speak.extend(list(map(int,input().split())))

count = 0
stack = 0
flag = True
for num in speak:
    if stack > 2:
        break
    count += 1
    for i in range(5):
        if num in bingo_X[i]:
            bingo_X[i].remove(num)
            if not bingo_X[i]:
                stack += 1
        if num in bingo_Y[i]:
            bingo_Y[i].remove(num)
            if not bingo_Y[i]:
                stack += 1
    if num in x:
        x.remove(num)
        if not x:
            stack += 1
    if num in y:
        y.remove(num)
        if not y:
            stack += 1

print(count)
