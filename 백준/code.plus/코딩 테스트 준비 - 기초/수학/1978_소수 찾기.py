input()
li = list(map(int,input().split()))
check = [1]*1001
check[1] = 0
check[0] = 0
for i in range(2,1001):
    if check[i] == 1:
        for j in range(i*2,1001,i):
            check[j] = 0
sum = 0
for num in li:
    sum += check[num]
print(sum)