def solution(answers):
    one = [1,2,3,4,5]*2000 # 5개 * 2000번
    two = [2,1,2,3,2,4,2,5]*1250 # 8개 * 1250번
    three = [3,3,1,1,2,2,4,4,5,5]*1000 # 10개 * 1000번
    c1, c2, c3 = 0,0,0 
    for i in range(len(answers)):
        if answers[i] == one[i]: c1 += 1
        if answers[i] == two[i]: c2 += 1
        if answers[i] == three[i]: c3 += 1
    max_num = max(c1,c2,c3)
    answer = []
    if max_num == c1: answer.append(1)
    if max_num == c2: answer.append(2)
    if max_num == c3: answer.append(3)
    
    return answer
