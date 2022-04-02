n = int(input())
if n < 3:
    print(1)
else:
    x,y=1,1
    for i in range(1,n-1):
        x,y = y,x+y
    print(y)
