l=[[i]+list(map(int,input().split())) for i in range(int(input()))]
a=sorted([(-(b**2+c**2),a+1) for a,b,c in l])
for _,i in a:print(i)
