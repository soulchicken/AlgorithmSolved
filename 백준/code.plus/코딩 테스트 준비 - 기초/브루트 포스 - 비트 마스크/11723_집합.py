import sys
input = sys.stdin.readline
bit = 0
for _ in range(int(input())):
    s = input()
    if s[:3] == "all":
        bit = (1 << 21) - 1
    elif s[:5] == "empty":
        bit = 0
    else:
        a,b = s.split()
        b = int(b)

        if a == "add":
            bit |= (1 << b)
        elif a == "remove":
            bit &= (1 << b) - 1
        
        elif a == "toggle":
            bit ^= (1 << b)

        elif a == "check":
            print((bit >> b) & 1)
