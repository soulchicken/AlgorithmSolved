t = 0
for _ in range(int(input())):
    a,b,c = sorted(list(map(int,input().split())))
    if a == b and b == c:
        t = max(t, 10000 + a*1000)
    elif a == b or b == c:
        t = max(t, 1000 + b*100)
    else:
        t = max(t, c*100)
print(t)
