input()
l=sorted(list(map(int,input().split())))
t=sum(l)
a=0
for i in l:t,a=t-i,a+i*(t-i)
print(a)
