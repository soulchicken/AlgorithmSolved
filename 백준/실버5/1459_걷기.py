x,y,a,b=map(int,input().split())
b = min(b,a*2)
x,y = max(x,y),min(x,y)
print(y*b + ((x-y)//2)*min(a,b)*2 + ((x-y)%2)*a)