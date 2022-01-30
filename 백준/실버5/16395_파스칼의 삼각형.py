n, k = map(int,input().split())
n -= 1
k -= 1
t = 1
for i in range(k+1,n+1):
    if i != 0:
        t *= i
s = 1
for i in range(1,n-k+1):
    s *= i

print(t//s)