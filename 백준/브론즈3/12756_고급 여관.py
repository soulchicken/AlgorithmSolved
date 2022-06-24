import math
a,b = map(int,input().split())
c,d = map(int,input().split())

x = math.ceil(d/a)
y = math.ceil(b/c)
if x > y:
    print('PLAYER B')
elif x == y:
    print('DRAW')
else:
    print('PLAYER A')
