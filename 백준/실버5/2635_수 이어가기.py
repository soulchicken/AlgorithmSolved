n=int(input())
li=[]
for i in range(1,n+1):
    li2 = [n]
    num1 = n
    num2 = i
    while num1 >= num2:
        num1,num2 = num2,num1-num2
        li2.append(num1)
    li2.append(num2)
    if len(li) < len(li2):
        li = li2.copy()
print(len(li))
print(' '.join(map(str,li)))
    
