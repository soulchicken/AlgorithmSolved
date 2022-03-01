n, m = map(int,input().split())
count = 0
if n != 0:
    box = list(map(int,input().split()))
    box.reverse()
    while box:
        x = m - box.pop()
        while box and x - box[-1] >= 0:
            x -= box.pop()
        count += 1
print(count)
        