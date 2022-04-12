n = int(input())
count = 0
for i in range(1,n+1):
    t = 0
    for j in range(i,n+1):
        t += j
        if t == n:
            count += 1
            break
        elif t > n:
            break
print(count)
