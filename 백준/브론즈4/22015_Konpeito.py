li = list(map(int,input().split()))
t = 0
for i in li:
    t += max(li) - i
print(t)
