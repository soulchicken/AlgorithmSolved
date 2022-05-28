import sys
input = sys.stdin.readline

n = int(input())
while 1:
    a = int(input())
    if not a:
        break

    if a // n != a / n:
        print(f"{a} is NOT a multiple of {n}.")
    else:
        print(f"{a} is a multiple of {n}.")
