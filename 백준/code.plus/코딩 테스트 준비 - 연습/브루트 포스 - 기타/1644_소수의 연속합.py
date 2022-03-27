import sys
input = sys.stdin.readline
N = int(input())
nums = []
li = [0]*(N+1)
for i in range(2,N+1):
    if li[i] == 0:
        nums.append(i)
        for j in range(i,N+1,i):
            li[j] = 1

if N == 1:
    print(0)
    
else:
    i = 0
    j = 0
    total = nums[0]
    length = len(nums)
    nums.append(4000001)
    nums.append(4000001)
    ##print(nums)
    count = 0
    while i != len(nums) - 1:
    ##    print(i,j,total)
        if total == N:
            count += 1
            total -= nums[i]
            i += 1
        elif (j < len(nums) and total < N) or i == j:
            j += 1
            total += nums[j]
        else:
            total -= nums[i]
            i += 1
    print(count)

