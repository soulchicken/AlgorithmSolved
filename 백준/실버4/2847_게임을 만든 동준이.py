n = int(input())
li = [int(input()) for _ in range(n)][::-1]
t = 0
for i in range(n-1):
    if li[i] <= li[i+1]:
        t += li[i+1] - li[i] + 1
        li[i+1] = li[i] - 1
print(t)
