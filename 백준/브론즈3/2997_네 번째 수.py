li = sorted(list(map(int,input().split())))
a,b = li[1] - li[0],li[2] - li[1]
if a == b:
    print(li[-1]+a)
elif a > b:
    print(li[0]+b)
else:
    print(li[1]+a)
