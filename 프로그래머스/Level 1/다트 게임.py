def solution(dartResult):
    dartResult = dartResult.replace('10','t')
    arr = []
    n = 0
    for i in range(1,len(dartResult)):
        if dartResult[i].isdigit() or dartResult[i] == 't':
            arr.append(dartResult[n:i])
            n = i
    arr.append(dartResult[n:])
    answer = []
    sqrt = {'S':1,'D':2,'T':3}
    for dart in arr:
        if dart[0] == 't':
            num = 10
        else:
            num = int(dart[0])
        num **= sqrt[dart[1]]
        answer.append(num)

    for i in range(3):
        print(arr[i],answer[i])
        if arr[i][-1] == '#':
            answer[i] *= -1
        elif arr[i][-1] == '*':
            answer[i] *= 2
            if i > 0:
                answer[i-1] *= 2

    return sum(answer)
