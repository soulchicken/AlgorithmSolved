n,m = map(int,input().split())
t = 1
for _ in range(n):
    for i in range(m):
        if i != m-1:
            print(t,end = ' ')
        else:
            print(t)
        t += 1
