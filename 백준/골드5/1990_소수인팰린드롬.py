li = [0]*10000001
n,m = map(int,input().split())
m = min(10000000,m)
for i in range(2,m+1):
    if li[i] == 0:
        if n <= i and str(i) == str(i)[::-1]:
            print(i)
        for j in range(i*2,m+1,i):
            li[j] = 1
print(-1)
