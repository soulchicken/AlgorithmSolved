import sys
input = sys.stdin.readline
n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]
check = [[None]*(1 << n) for _ in range(n)]
end_point = (1 << n) - 1

def BitMask(end,visited):
    if visited == end_point:
        if li[end][0]:
            return li[end][0]
        return 16000000
    if check[end][visited] is not None:
        return check[end][visited]
    num = 16000000
    for i in range(n):
        if (visited & (1 << i) == 0) and li[end][i] != 0:
            num = min(num,li[end][i] + BitMask(i,visited | (1 << i)))

    check[end][visited] = num
    return num

answer = BitMask(0,1)
print(answer)
