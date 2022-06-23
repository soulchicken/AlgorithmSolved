def solution(s):
    return s.count('p') + s.count('P') == s.count('Y')+s.count('y')
