from collections import deque
n = int(input())
li = list(map(int,input().split()))
que = deque()
flag = True
while flag:
    que.appendleft(li.pop())
    if (not li):
        flag = False
    elif que[0] < li[-1]:
        que.appendleft(li.pop())
        break

if flag:
    index = 0
    max_num = 0
    que = list(que)
    for i in range(1,len(que)):
        if max_num < que[i] and que[i] < que[0]:
            max_num = que[i]
            index = i
    li.append(que.pop(index))
    que.sort(reverse = True)

    li += que
    s = ""
    for i in range(n):
        if i != 0:
            s += " " + str(li[i])
        else:
            s += str(li[i])
    print(s)
        

else:
    print(-1)