N = int(input())
li = list(map(int,input().split()))
count = [1]*N
for i in range(1,N):
    for j in range(i):
        if li[i] > li[j]:
            count[i] = max(count[i],count[j]+1)
print(max(count))