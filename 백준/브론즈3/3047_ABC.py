li = sorted(list(zip(sorted(list(map(int,input().split()))),['A','B','C'])))
for a in input():
    for i in range(3):
        if li[i][1] == a:
            print(li[i][0],end = ' ')
