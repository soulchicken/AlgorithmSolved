n = int(input())
li = [0]*200
li2 = []

for i in range(2,200):
    if li[i] == 0:
        li2.append(i)
        for j in range(i*2,200,i):
            li[j] = 1

li3 = []
for i in range(len(li2)-1):
    li3.append(li2[i] * li2[i+1])
    if li3[-1] > n:
        print(li3[-1])
        break