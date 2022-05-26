from collections import deque

n = int(input())
li = list(map(int,input().split()))
li += [0]*(3 - n)
s,c,v = li
MAX = float('inf')
hp = [[[MAX]*(v+1) for _ in range(c+1)] for _ in range(s+1)] # hp[s][c][v]

que = deque()
que.append((s,c,v,0)) # s,c,v,count

attack = ((9,3,1),(9,1,3),(3,9,1),(3,1,9),(1,3,9),(1,9,3))

while que:
##    print(que)
    s,c,v,count = que.popleft()
##    print(s,c,v,count)
    if hp[s][c][v] > count:
        hp[s][c][v] = count

        # hp 깎기
        for q,w,e in attack:
            x = max(0,s-q)
            y = max(0,c-w)
            z = max(0,v-e)
            que.append((x,y,z,count + 1))

print(hp[0][0][0])

