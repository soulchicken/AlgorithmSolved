for _ in range(int(input())):
    x,y,a,b = map(int,input().split())
    count = 0
    for _ in range(int(input())):
        q,w,r = map(int,input().split())
        if (q-x)**2 + (w-y)**2 <= r**2:
            count += 1
            if (q-a)**2 + (w-b)**2 <= r**2:
                count -= 1
            continue
        elif (q-a)**2 + (w-b)**2 <= r**2:
            count += 1
    print(count)
