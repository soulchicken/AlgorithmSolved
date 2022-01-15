input()
a = list(set(map(int,input().split())) - set(map(int,input().split())))

if len(a) == 0:
    print(0)
else:        
    print(len(a))
    a.sort()
    for i in range(len(a)):
        if i != len(a) - 1:
            print(a[i], end = ' ')
        else:
            print(a[i])
