def solution(x, n):
    return [x + i*x for i in range(n)]
print(solution(2,5),[2,4,6,8,10])
print(solution(4,3),[4,8,12])
print(solution(-4,2),[-4,-8])
