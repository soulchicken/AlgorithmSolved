while 1:
    s=input()
    if s=='.':break
    for i in range(1,len(s)//2+1):
        if len(s)%i==0 and s==s[:i]*(len(s)//i):print(len(s)//i);break
    else:print(1)
