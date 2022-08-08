for _ in range(int(input())):
    a,b = 0,0
    for _ in range(int(input())):
        c,d = input().split()
        if (c == 'R' and d == 'P') or (c == 'P' and d == 'S') or (c == 'S' and d == 'R'):
            b += 1
        elif c != d:
            a += 1
    if a > b:
        print('Player 1')
    elif a == b:
        print('TIE')
    else:
        print('Player 2')
