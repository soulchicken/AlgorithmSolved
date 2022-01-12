k = int(input())
t = 0
n = 0
while 1:
    if k == 0:
        print(t)
        break
    n += 1
    if n > k:
        n = 1
    t += 1
    k -= n
