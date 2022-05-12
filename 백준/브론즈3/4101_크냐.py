while 1:
    a,b = map(int,input().split())
    if not a+b:
        break
    elif a > b:
        print('Yes')
    else:
        print('No')
