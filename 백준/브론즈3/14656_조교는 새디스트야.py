n = int(input())
li = list(map(int,input().split()))
count = 0
for i in range(1,n+1):
    if i != li[i-1]: count += 1
print(count)
