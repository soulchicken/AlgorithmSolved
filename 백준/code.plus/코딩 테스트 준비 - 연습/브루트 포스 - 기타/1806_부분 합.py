import sys
input = sys.stdin.readline
N, S = map(int,input().split())
li = list(map(int,input().split()))
li.append(0)
li.append(0)
i = 0
j = 0
total = li[0]
length = 1
answer = 99999999999
while i != N:
    if total >= S and answer > length:
        answer = length

    if i == j and j != N - 2:
        j += 1
        length += 1
        total += li[j] + 0
    elif j == N-1 or total > S:
        total -= li[i]
        length -= 1
        i += 1

    else:
        if j == N:
            total -= li[i]
            i += 1
            length -= 1
            continue
        j += 1
        length += 1
        total += li[j]
if answer == 99999999999:print(0)
else: print(answer)
