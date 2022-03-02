n,m = map(int,input().split())
check = [1]*1000001
check[1] = 0
check[0] = 0
for i in range(2,1000001):
    if check[i] == 1:
        for j in range(i*2,1000001,i):
            check[j] = 0

for num in range(n,m+1):
    if check[num] == 1:
        print(num)