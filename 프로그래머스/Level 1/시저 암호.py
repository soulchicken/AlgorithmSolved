def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += i
        elif i.isupper():
            answer += chr((ord(i) - ord('A') + n)%26 + ord('A'))
        else:
            answer += chr((ord(i) - ord('a') + n)%26 + ord('a'))
    return answer
