import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a,b = input().split()
    print(bin(int('0b'+ a,2) + int('0b'+b,2))[2:])
