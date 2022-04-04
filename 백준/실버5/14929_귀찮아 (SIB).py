n = int(input())
li = list(map(int,input().split()))
li2 = [0]*n
li2[0] = sum(li) - li[0]
total = li2[0] * li[0]
for i in range(1,n):
    li2[i] = li2[i-1] - li[i]
    total += li2[i] * li[i]
print(total)