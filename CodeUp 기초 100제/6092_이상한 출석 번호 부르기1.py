n = int(input())
li = list(map(int,input().split()))
check = [0]*24
for i in li:
    check[i] += 1

for i in range(1,24):
    print(check[i],end=' ')