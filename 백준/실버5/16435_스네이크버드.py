n,L = map(int,input().split())
li = sorted(list(map(int,input().split())))
for i in li:
    if i > L:
        break
    L += 1
print(L)
