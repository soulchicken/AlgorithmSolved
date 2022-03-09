N, S = map(int,input().split())
li = list(map(int,input().split()))
count = 0
for i in range(1,1<<N):
    total = 0
    for n in range(N):
        if i & (1 << n) != 0:
            total += li[n]
    if total == S:
        count += 1
print(count)