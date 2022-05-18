import sys
input = sys.stdin.readline

li1 = []
li2 = []
li3 = []
li4 = []

n = int(input())
for _ in range(n):
    a,b,c,d = map(int,input().split())
    li1.append(a)
    li2.append(b)
    li3.append(c)
    li4.append(d)

arr1 = []
arr2 = []

for i in range(n):
    for j in range(n):
        arr1.append(li1[i]+li2[j])
        arr2.append(li3[i]+li4[j])

arr1.sort()
arr2.sort()


li1 = []
index1 = []

for i in range(len(arr1)):
    if not li1 or li1[-1] != arr1[i]:
        li1.append(arr1[i])
        index1.append(1)
    else:
        index1[-1] += 1

li2 = []
index2 = []

for i in range(len(arr2)):
    if not li2 or li2[-1] != arr2[i]:
        li2.append(arr2[i])
        index2.append(1)
    else:
        index2[-1] += 1


count = 0
for i in range(len(li1)):
    t = li1[i]
    left = 0
    right = len(li2) - 1
    while left <= right:
        mid = (left + right) // 2
        if t + li2[mid] == 0:
            count += index1[i]*index2[mid]
            break

        if t + li2[mid] > 0:
            right = mid - 1
        else:
            left = mid + 1

print(count)
