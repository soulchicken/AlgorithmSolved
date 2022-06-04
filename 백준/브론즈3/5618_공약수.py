import math
n = int(input())
li= list(map(int,input().split()))
ans = li[0]

for i in range(n):
    ans = math.gcd(ans,li[i])

li = []

for i in range(1,int((ans+1)**0.5) + 1):
    if ans % i == 0:
        li.append(i)
        if i != ans // i:
            li.append(ans // i)
li.sort()
for i in li:
    print(i)
