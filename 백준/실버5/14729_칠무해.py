n = int(input())
li = [float(input()) for _ in range(n)]
li.sort()
for i in range(7):
    print('{:.3f}'.format(li[i]))