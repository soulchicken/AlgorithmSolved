import sys
input = sys.stdin.readline
while 1:
    try:
        n = int(input())
        one = 1
        count = 1
        while 1:
            if one % n == 0:
                print(count)
                break
            count += 1
            one = one*10 + 1
    except:
        break
