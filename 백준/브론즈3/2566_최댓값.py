ans,a,b = 0,0,0
for i in range(9):
    li = list(map(int,input().split()))
    for j in range(9):
        if li[j] > ans:
            ans,a,b = li[j],i,j
            
print(ans)
print(a+1,b+1)
