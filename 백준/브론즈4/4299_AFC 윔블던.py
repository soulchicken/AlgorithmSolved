a,b = list(map(int,input().split()))
x = a-b
if x % 2 == 1 or x < 0:
    print(-1)
else:
    x //= 2
    print(b+x,x)
