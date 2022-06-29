for _ in range(int(input())):
    li = sorted(list(map(int,input().split())))
    total = 0
    num = 200
    for i in li:
        if not i % 2:
            total += i
            num = min(num,i)
    print(total,num)
