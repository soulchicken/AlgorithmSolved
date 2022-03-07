import math

n = int(input())
li = list(map(int,input().split()))
li.reverse()
top,bottom = li[0], 1
for i in range(1,n):
    top,bottom = bottom + top * li[i], top
    gcd = math.gcd(top,bottom)
    top //= gcd
    bottom //= gcd
top, bottom = top - bottom , top
gcd = math.gcd(top,bottom)
top //= gcd
bottom //= gcd
print(top,bottom)