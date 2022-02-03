import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0: break

    li = []
    for _ in range(n):
        s = input()
        li.append((s.upper(),s))
    li.sort()
    print(li[0][1].rstrip())