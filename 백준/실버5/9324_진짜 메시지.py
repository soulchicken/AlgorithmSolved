import sys
input = sys.stdin.readline
# A : 65, Z : 90

def W():    
    s = input().rstrip()
    i = 0
    alpha = [0]*26
    while i < len(s):
        index = ord(s[i]) - 65
        alpha[index] += 1
        if alpha[index] == 3 and i + 1 == len(s):
            return "FAKE"
        elif alpha[index] == 3 and i + 1 < len(s) and index != ord(s[i+1]) - 65:
            return "FAKE"
        elif alpha[index] == 3 and i + 1 < len(s) and index == ord(s[i+1]) - 65:
            i += 2
            alpha[index] = 0
        elif alpha[index] == 3:
            alpha[index] = 0
            i += 1
        else:
            i += 1
    return "OK"

for _ in range(int(input())):
    print(W())
