a,b,c = map(int,input().split(':'))
d,e,f = map(int,input().split(':'))
ans = d*3600 + e*60 + f - a*3600 - b*60 - c
if ans < 0:
    ans += 24*3600
x = str(ans // 3600)
ans %= 3600
y = str(ans // 60)
ans %= 60
z = str(ans)
print(f'{x.zfill(2)}:{y.zfill(2)}:{z.zfill(2)}')
