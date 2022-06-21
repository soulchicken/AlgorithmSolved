def solution(num):
    for i in range(501):
        if num == 1:
            return i
        elif num % 2:
            num = num * 3 + 1
        else:
            num //= 2
    return -1
