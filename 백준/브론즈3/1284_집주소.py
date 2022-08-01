while 1:
    s = input()
    if s == '0': break
    t = 1
    for n in s:
        if n == '0':
            t += 5
        elif n == '1':
            t += 3
        else:
            t += 4
    print(t)
