n,m = sorted(list(map(int,input().split())))
print(max(m-n-1,0))
for i in range(n+1,m):
    print(i,end= ' ')