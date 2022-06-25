def solution(nums):
    check = [1]*3001
    for i in range(2,3001):
        if check[i]:
            for j in range(i*2,3001,i):
                check[j] = 0
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if check[nums[i]+nums[j]+nums[k]]:
                    answer += 1
    return answer
