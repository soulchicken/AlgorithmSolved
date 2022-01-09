n,w,h = map(int,input().split())
x = (w**2 + h**2)**0.5
for _ in range(n):
    a = int(input())
    if a > x:
        print('NE')
    else:
        print('DA')
