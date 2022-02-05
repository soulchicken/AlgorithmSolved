n,a,b,c,d = map(int,input().split())
if n // a == n / a:
    a = n // a
else:
    a = n // a + 1

if n // c == n / c:
    c = n // c
else:
    c = n // c + 1

print(min(a*b,c*d))