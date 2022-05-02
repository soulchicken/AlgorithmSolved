n = int(input())
li = sorted(list(map(int,input().split())))
num = float('inf')
answer = []
for i in range(n-2):
    for j in range(i+1,n-1):
        total = li[i] + li[j]
        left = j + 1
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if abs(total + li[mid]) < num:
                answer = [i,j,mid]
                num = abs(total + li[mid])
            if total + li[mid] > 0:
                right = mid - 1
            else:
                left = mid + 1

for i in answer:
    print(li[i] ,end= ' ')
