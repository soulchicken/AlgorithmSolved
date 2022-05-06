n = int(input())
li = list(map(int,input().split()))
num = float('inf')
for i in range(n-1):
    left = i+1
    right = n-1
    while left <= right:
        mid = (left + right) // 2
        if abs(li[i] + li[mid]) < abs(num):
            num = li[i] + li[mid]

        if li[i] + li[mid] > 0:
            right = mid - 1
        else:
            left = mid + 1
print(num)
