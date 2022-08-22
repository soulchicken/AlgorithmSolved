a,b = map(int,input().split())
ans = 1
n = a * (a - 1) // 2
for i in range(a,b+1):
    n += i
    ans *= n
    ans %= 14579
print(ans)
