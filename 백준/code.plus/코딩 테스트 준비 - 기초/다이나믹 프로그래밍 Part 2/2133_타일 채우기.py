n = int(input())
li = [0,0,3,0,11]
for i in range(5,n+1):
    li.append(li[i-2]*3 + li[i-4]*2)
print(li)
5
