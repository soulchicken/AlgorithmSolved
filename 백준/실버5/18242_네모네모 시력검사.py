n,m = map(int,input().split())
li = [list(input().rstrip()) for _ in range(n)]
rows = [0]*n
cols = [0]*m
for i in range(n):
    for j in range(m):
        if li[i][j] == '#':
            rows[i] += 1
            cols[j] += 1
topbottom = [2,2]
rightleft = [2,2]
for i in rows:
    if i > 2:
        topbottom.append(i)
for j in cols:
    if j > 2:
        rightleft.append(j)
top,bottom = topbottom[-2], topbottom[-1]
left,right = rightleft[-2],rightleft[-1]
min_num = min(top,bottom,left,right)
if top == min_num:
    print('UP')
elif bottom == min_num:
    print('DOWN')
elif left == min_num:
    print('LEFT')
else:
    print('RIGHT')
