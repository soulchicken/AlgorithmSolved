while 1:
    li = list(map(int,input().split()))
    if not sum(li):
        break
    a,b,c = sorted(li)
    if c >= b+a:
        print('Invalid')
    elif a == b and a == c:
        print('Equilateral')
    elif a == b or b == c:
        print('Isosceles')
    else:
        print('Scalene')
