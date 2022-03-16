n=int(input());a,b=2,1
for _ in range(3,n+1):a,b=(a+b)%10007,a
print(a if n>1 else n)