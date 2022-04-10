li = [[0]*6 for _ in range(6)]
flag = True
s = input()
x,y = ord(s[0]) - 65,int(s[1]) - 1
start_x,start_y = x,y
li[x][y] = 1
for _ in range(35):
    s = input()
    if not flag:
        continue
    a,b = ord(s[0]) - 65,int(s[1]) - 1
    if abs(a-x)*abs(b-y) != 2:
        flag = False
    li[a][b] = 1
    x,y = a,b

if abs(start_x - x) * abs(start_y - y) != 2:
    flag = False

t = sum([sum(li[i]) for i in range(6)])
if t == 36 and flag:print('Valid')
else:print('Invalid')
