n = int(input())
li = sorted(list(map(int,input().split())))
m = int(input())
arr = list(map(int,input().split()))

for i in range(m):
    a = arr[i]
    left = 0
    right = n-1
    flag = 0
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == a:
            flag = 1
            break
        elif li[mid] < a:
            left = mid + 1
        else:
            right = mid - 1
    print(flag, end = ' ')
