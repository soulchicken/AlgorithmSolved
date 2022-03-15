from collections import deque
que = deque()
N, K = map(int,input().split())
arr = [float('inf')]*(100001)
que.append([0,N])
while que:
    count,place = que.popleft()
    if 0 <= place and place < 100001 and arr[place] > count:
        arr[place] = count
        que.append([count+1,place+1])
        que.append([count+1,place-1])
        que.append([count+1,place*2])
print(arr[K])