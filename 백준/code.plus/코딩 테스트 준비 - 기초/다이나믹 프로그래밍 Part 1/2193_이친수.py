li0 = [0,0,1,1,2] + [0]*86
li1 = [0,1,0,1,1] + [0]*86

for i in range(5,91):
    li0[i] = li0[i-1] + li1[i-1]
    li1[i] = li0[i-1]

n = int(input())
print(li0[n]+li1[n])
