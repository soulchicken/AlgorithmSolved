n,m = map(int,input().split())
a,b = n,m
if a < b: a,b = b,a
while b:
    a,b = b,a%b
gcd = a
lcm = n*m//a
print(gcd)
print(lcm)