def solution(s):
    answer = ""
    flag = True
    for i in s:
        if i == ' ':
            answer += i
            flag = True
        elif flag:
            answer += i.upper()
            flag = False
        else:
            answer += i.lower()
            flag = True
    return answer
