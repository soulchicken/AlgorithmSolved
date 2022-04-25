from itertools import combinations
n = int(input())
ans = [0]*n
for i in range(n):
    li = list(map(int,input().split()))
    for com in combinations(li,3):
        ans[i] = max(ans[i],sum(com)%10)
max_num = max(ans)
for i in range(n-1,-1,-1):
    if max_num == ans[i]:
        print(i+1)
        break
