r, c, n = map(int,input().split())
if r % n == 0: r //= n
else : r = (r // n) + 1
if c % n == 0: c //= n
else : c = (c // n) + 1
print(c*r)