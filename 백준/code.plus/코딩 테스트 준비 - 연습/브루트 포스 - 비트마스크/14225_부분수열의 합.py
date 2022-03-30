N = int(input())
li = list(map(int,input().split()))
check = [True]*(N*100000 +2)
for bit in range(1, (1 << N)+1):
    total = 0
    for i in range(N):
        if (1 << i) & bit:
            total += li[i]
    check[total] = False
for i in range(1,N*100000 +2):
    if check[i]:
        print(i)
        break
