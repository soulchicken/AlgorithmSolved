import sys
input = sys.stdin.readline
n = int(input())
answer = []
for _ in range(n):
    answer.append(float(input()))
    while len(answer) > 7:
        answer.sort()
        answer.pop()
for i in range(7):
    print('{:.3f}'.format(answer[i]))