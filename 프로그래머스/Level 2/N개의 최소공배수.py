def solution(arr):
    answer = 1
    for a in arr:
        x = answer
        y = a
        while y:
            x,y = y,x%y
        answer = answer*a//x
    return answer
