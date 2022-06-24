def solution(n):
    return int(''.join(map(str,sorted(list(map(int,str(n))))[::-1])))
