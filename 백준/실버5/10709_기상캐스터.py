import sys
input = sys.stdin.readline
h,w = map(int,input().split())
li = [list(input()) for _ in range(h)]

for i in range(h):
    count = 0
    for j in range(w):
        if count == 0 and li[i][j] == '.':
            li[i][j] = -1
        
        elif count == 0 and li[i][j] == 'c':
            li[i][j] = count
            count += 1
        elif li[i][j] == '.':
            li[i][j] = count
            count += 1
        else:
            li[i][j] = 0
            count = 1
        
        print(li[i][j], end=' ')  
    print()