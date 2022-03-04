import sys
input = sys.stdin.readline

def makeKaing(N,y):
    while y > N:
        y -= N
    return y

def kaing():
    a,b = 0, 0
    M,N,x,y = map(int,input().split())
    count = x - a
    b += count
    a = x
    b = makeKaing(N,b)
    if b == y:
        return count       
    lcm = N
    
    for i in range(lcm):
        b += M
        count += M
        b = makeKaing(N,b)
        if b == y:
            return count
    return -1

n = int(input())
for _ in range(n):
    print(kaing())
