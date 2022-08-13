input()
li = list(map(int,input().split()))
n = -1
for i in li:
    n = max(n, i)
print(n)
