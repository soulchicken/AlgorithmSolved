def solution(d, budget):
    count, total = 0, 0
    for money in sorted(d):
        if total + money > budget: break
        total += money
        count += 1
    return count
