def solution(s):
    answer = ''
    flag = True
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            flag = True
        elif flag:
            answer += s[i].upper()
            flag = False
        else:
            answer += s[i].lower()
    return answer
