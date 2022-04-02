n = int(input())
x,y = 0,1
for i in range(n-1):x,y = y,x+y
print(2*x+4*y)
