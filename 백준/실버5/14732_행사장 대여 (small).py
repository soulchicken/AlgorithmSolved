li = [[0]*501 for _ in range(501)]
for _ in range(int(input())):
    x,y,u,v = map(int,input().split())
    for i in range(x,u):
        for j in range(y,v):
            li[i][j] = 1

t = 0
for i in li:
    t += sum(i)

print(t)
