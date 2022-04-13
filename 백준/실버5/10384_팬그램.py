import sys
input = sys.stdin.readline
for k in range(int(input())):
    alpha = [0]*26
    s = input().upper()
    for i in s:
        n = ord(i) - ord('A')
        if n >= 0 and n < 26:
            alpha[n] += 1

    counts = [0,0,0]
    for i in range(26):
        for j in range(min(alpha[i],3)):
            counts[j] += 1

    if counts[2] == 26:
        speak = 'Triple pangram!!!'
    elif counts[1] == 26:
        speak = 'Double pangram!!'
    elif counts[0] == 26:
        speak = 'Pangram!'
    else:
        speak = 'Not a pangram'

    print(f'Case {k+1}: {speak}')
