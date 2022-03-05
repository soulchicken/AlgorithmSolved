n = int(input())
ans = 1
i = 1
while n != 1:
    if n < 10000000000:
        ans *= int(n**0.5)
        n = 1
    i += 1
    if n % i == 0:
        ans *= i
        n //= i*i
        i = 1
print(ans)

import math;print(math.isqrt(int(input())))