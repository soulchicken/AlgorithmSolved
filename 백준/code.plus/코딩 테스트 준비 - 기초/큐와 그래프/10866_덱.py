import sys
from collections import deque
# n 입력 받기
n = int(sys.stdin.readline())

# 덱 a 만들기
a = deque([])

# n 번 명령 입력 받
for i in range(n):
    s = sys.stdin.readline().strip('\n').split()

    if len(s) == 1:
        if s[0] == 'pop_front':
            if len(a) == 0:
                print(-1)
            else:
                x = a.popleft()
                print(x)
                
        elif s[0] == 'pop_back':
            if len(a) == 0:
                print(-1)
            else:
                x = a.pop()
                print(x)

        elif s[0] == 'size':
            print(len(a))
            
        elif s[0] == 'empty':
            if len(a) == 0:
                print(1)
            else:
                print(0)
                
        elif s[0] == 'front':
            if len(a) == 0:
                print(-1)
            else:
                print(a[0])
        else :
            if len(a) == 0:
                print(-1)
            else:
                print(a[-1])
    else:
        if s[0] == 'push_back':
            a.append(s[1])

        else:
            a.appendleft(s[1])