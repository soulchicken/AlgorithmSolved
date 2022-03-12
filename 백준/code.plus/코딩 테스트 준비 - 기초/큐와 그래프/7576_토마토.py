from collections import deque

M, N = map(int,input().split())

arr = []
que = deque() # n,m,counts
move = ((0,1),(0,-1),(1,0),(-1,0))
count_tomato = M*N
for n in range(N):
    li = list(map(int,input().split()))
    arr.append(li)
    for m in range(M):
        if li[m] == 1:
            for dn,dm in move:
                que.append((n+dn,m+dm,2))
            count_tomato -= 1
        elif li[m] == -1:
            count_tomato -= 1

while count_tomato != 0 and que:
    n,m,count = que.popleft()
    if 0 <= n and n < N and 0 <= m and m < M and arr[n][m] != -1 and (arr[n][m] == 0 or count < arr[n][m]):
        arr[n][m] = count
        count_tomato -= 1
        for dn,dm in move:
            que.append((n+dn,m+dm,count+1))

count_time = 0
for n in arr:
    count_time = max(count_time,max(n))

if count_tomato == 0:
    print(count_time - 1)
else:
    print(-1)