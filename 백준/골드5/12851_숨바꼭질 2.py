from collections import deque
que = deque()
N, K = map(int,input().split())
arr = [float('inf')]*100001
counts = [0]*100001
que.append([0,N])
while que:
    count,place = que.popleft()
    if 0 <= place and place < 100001:
        if arr[place] > count:
            arr[place] = count
            counts[place] = 1
            que.append([count+1,place+1])
            que.append([count+1,place-1])
            que.append([count+1,place*2])
        elif arr[place] == count:
            counts[place] += 1
            que.append([count+1,place+1])
            que.append([count+1,place-1])
            que.append([count+1,place*2])
print(arr[K])
print(counts[K])
