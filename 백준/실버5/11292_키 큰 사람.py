while 1:
    n = int(input())
    if n == 0: break
    li = []
    max_num = 0
    for _ in range(n):
        a, b = input().split()
        b = float(b)
        li.append((a,b))
        if b > max_num:
            max_num = b
    for i in range(n):
        if li[i][1] == max_num:
            print(li[i][0], end = ' ')
    print()
        
