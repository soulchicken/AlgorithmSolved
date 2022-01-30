a,b,c,d = map(int,input().split())
for _ in range(d-1):
    a *= b
    a += c
    print(a)