import sys
input = sys.stdin.readline
i = 0
while True:
    i += 1
    n = int(input())
    if n == 0:
        break
    print(i)
    li = [input().rstrip() for _ in range(n)]
    li.sort()
    for song in li:
        print(song)
