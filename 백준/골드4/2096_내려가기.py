n = int(input())
q,w,e,r,t,y = list(map(int,input().split()))*2
for i in range(n-1):
    a,s,d,f,g,h = list(map(int,input().split()))*2
    a += max(q,w)
    s += max(q,w,e)
    d += max(w,e)
    f += min(r,t)
    g += min(r,t,y)
    h += min(t,y)
    q,w,e,r,t,y = a,s,d,f,g,h
print(max(q,w,e),min(r,t,y))