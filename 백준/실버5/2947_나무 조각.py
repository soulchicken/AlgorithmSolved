li = list(map(int,input().split()))

def f():
    for i in li:
        print(i,end = ' ')
    print()

while li != [1,2,3,4,5]:
    if li[0] > li[1]: 
        li[0],li[1] = li[1],li[0]
        f()
    if li[1] > li[2]: 
        li[1],li[2] = li[2],li[1]
        f()
    if li[2] > li[3]: 
        li[2],li[3] = li[3],li[2]
        f()
    if li[3] > li[4]: 
        li[3],li[4] = li[4],li[3]
        f()
    