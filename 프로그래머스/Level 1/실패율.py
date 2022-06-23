def solution(N, stages):
    in_stages = [0]*(N+2)
    for people in stages:
        in_stages[people] += 1

    clear_stages = in_stages.copy()
    for i in range(N,0,-1):
        clear_stages[i] += clear_stages[i+1]

    per = []
    for i in range(1,N+1):
        if in_stages[i]:
            per.append((1-in_stages[i]/clear_stages[i],i))
        else:
            per.append((1,i))
    return [a for _,a in sorted(per)]
