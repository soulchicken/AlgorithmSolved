n,k = map(int,input().split())
li = list(map(int,input().split()))
ans = []
for i in range(n):
    try :
        t = 0
        for j in range(k):
            t += li[i+j]
        ans.append(t)
    except : break
print(max(ans))
