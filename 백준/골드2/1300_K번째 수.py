N = int(input())
K = int(input())
left, right = 1, K
ans = 0
while left <= right:
    mid = (left + right) // 2
    x = 0
    for i in range(1, N+1):
        x += min(mid//i, N)
    if x >= K:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)
