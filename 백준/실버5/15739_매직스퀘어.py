flag = 1
n = int(input())
t = n * (n**2 + 1) // 2
t1,t2 = 0,0
cols = [0]*n
check = [0]*(n**2)
for i in range(n):
    li = list(map(int,input().split()))
    if sum(li) != t: flag = 0
    t1 += li[i]
    t2 += li[n - 1 - i]
    for j in range(n):
        cols[j] += li[j]
        check[li[j]-1] = 1
if t1 != t or t2 != t: flag = 0
for i in cols:
    if i != t: flag = 0
if sum(check) != n**2: flag = 0
if flag:print('TRUE')
else:print('FALSE')
