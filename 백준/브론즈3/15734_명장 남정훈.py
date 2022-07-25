l,r,a = map(int,input().split())
l,r = max(l,r), min(l,r)
if r + a >= l:
    a = (r+a-l)
    print('111111')
    print(2*l + 2*(a//2))
else:
    print((r+a)*2)
