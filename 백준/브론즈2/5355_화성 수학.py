for _ in range(int(input())):
    li = list(input().split())
    n = float(li[0])
    for i in range(1,len(li)):
        if li[i] == '@':
            n *= 3
        elif li[i] == '%':
            n += 5
        else:
            n -= 7
    print('%.2f' %n)
