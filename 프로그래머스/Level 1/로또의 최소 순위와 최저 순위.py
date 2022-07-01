def solution(lottos, win_nums):
    score = [6,6,5,4,3,2,1]
    count = lottos.count(0)
    n = len(set(lottos) & set(win_nums))
    return [score[n+count], score[n]]