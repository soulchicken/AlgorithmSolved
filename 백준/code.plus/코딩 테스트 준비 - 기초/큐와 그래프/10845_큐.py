import sys


n = int(sys.stdin.readline())
li = []

for i in range(n):
    s = list(sys.stdin.readline().strip('\n').split())

    if len(s) == 1: # pop, size, empty, front, back
        if s[0] == 'size':
            print(len(li))
            
        elif s[0] == 'empty':
            if len(li) == 0:
                print(1)
            else :
                print(0)
        else: #pop,front,back
            if len(li) == 0:
                print(-1)

            elif s[0] == 'front':
                print(li[0])
            elif s[0] == 'back':
                print(li[-1])
            else: # pop
                print(li.pop(0))
    else : # push
        li.append(int(s[1]))