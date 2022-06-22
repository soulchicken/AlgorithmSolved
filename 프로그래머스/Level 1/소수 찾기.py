def solution(n):
    ans = [1]*(n+1)
    ans[0],ans[1] = 0,0
    for i in range(2,n+1):
        if ans[i]:
            for j in range(i*2,n+1,i):
                ans[j] = 0
    return sum(ans)
