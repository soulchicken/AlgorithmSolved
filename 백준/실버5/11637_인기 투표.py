import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    li = [int(input()) for _ in range(n)]
    total = sum(li)
    people = [i+1 for i in range(n)]
    ans = sorted(list(zip(li,people)))
    if ans[-1][0] == ans[-2][0]:
        print("no winner")
    elif ans[-1][0] > total/2:
        print("majority winner",ans[-1][1])
    else:
        print("minority winner",ans[-1][1])
