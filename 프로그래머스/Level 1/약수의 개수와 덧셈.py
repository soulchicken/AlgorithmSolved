def solution(left, right):
    return (left + right)*(right - left + 1)//2 - sum([2*i for i in range(left,right+1) if i**0.5 == int(i**0.5)])
