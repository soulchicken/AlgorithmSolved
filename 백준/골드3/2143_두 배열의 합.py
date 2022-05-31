T = int(input())
n = int(input())
lin = list(map(int,input().split()))
m = int(input())
lim = list(map(int,input().split()))
cntn = [0]*n
cntm = [0]*m
cntn[0] = lin[0]
cntm[0] = lim[0]
for i in range(1,n):
    cntn[i] = cntn[i-1] + lin[i]

for i in range(1,m):
    cntm[i] = cntm[i-1] + lim[i]

arr1 = []
arr2 = []
for i in range(n):
    arr1.append(cntn[i])
    for j in range(i+1,n):
        arr1.append(cntn[j] - cntn[i])
for i in range(m):
    arr2.append(cntm[i])
    for j in range(i+1,m):
        arr2.append(cntm[j] - cntm[i])
arr1.sort()
arr2.sort()
count = 0

arr3 = []
li1 = []
arr4 = []
li2 = []

for i in arr1:
    if arr3 and arr3[-1] == i:
        li1[-1] += 1
    else:
        arr3.append(i)
        li1.append(1)

for i in arr2:
    if arr4 and arr4[-1] == i:
        li2[-1] += 1
    else:
        arr4.append(i)
        li2.append(1)


for n in range(len(arr3)):
    left = 0
    right = len(arr4) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr3[n] + arr4[mid] == T:
            count += li1[n] * li2[mid]
        if arr3[n] + arr4[mid] > T:
            right = mid - 1
        else:
            left = mid + 1
print(count)
