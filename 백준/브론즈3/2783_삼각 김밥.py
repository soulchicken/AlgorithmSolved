X, Y = map(int,input().split())
num = X / Y
for _ in range(int(input())):
    x,y = map(int,input().split())
    num = min(num, x/y)
print(num * 1000)
