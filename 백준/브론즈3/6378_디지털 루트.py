while 1:
    n = input()
    if n == '0':
        break

    while len(n) != 1:n = str(sum(map(int,n)))
    print(n)
