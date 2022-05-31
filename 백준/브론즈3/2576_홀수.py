t = 0
m = 101
for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        t += n
        m = min(n,m)
if t:
    print(t)
    print(m)
else:
    print(-1)
