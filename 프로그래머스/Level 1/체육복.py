def solution(n, lost, reserve):
    people = [1]*(n+1)
    for i in lost:
        people[i] = 0

    remove = []
    for i in reserve:
        if not people[i]:
            people[i] = 1
            remove.append(i)
    for r in remove:
        reserve.remove(r)
    reserve.sort()
    for i in range(1,n+1):
        if not people[i] and i-1 in reserve:
            people[i] = 1
            reserve.remove(i-1)
        elif not people[i] and i+1 in reserve:
            people[i] = 1
            reserve.remove(i+1)
    return sum(people) - 1
