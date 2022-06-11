C,K,P = map(int,input().split())
ans = 0
for n in range(C+1):
    ans += K*n + P * n**2
print(ans)
