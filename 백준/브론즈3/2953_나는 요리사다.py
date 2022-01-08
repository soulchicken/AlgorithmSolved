m, j = 0, 0
for i in range(1,6):
    n = sum(map(int,input().split()))
    if m < n:
        m = n
        j = i
print(j,m)
