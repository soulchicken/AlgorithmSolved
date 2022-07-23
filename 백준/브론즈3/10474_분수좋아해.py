while 1:
    a,b = map(int,input().split())
    if not a+b:
        break
    print(a//b,a%b,'/',b)
