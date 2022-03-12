from collections import deque
import copy
que = deque()
N, K = map(int,input().split())
##max_num = N+K
max_num = 100001
arr = [float('inf')]*(max_num)
route = [0]*max_num
que.append([0,N,N])
while que:
    count,place,last = que.popleft()
    if 0 <= place and place < max_num and arr[place] > count:
        arr[place] = count
        route[place] = last
        que.append([count+1,place+1,place])
        que.append([count+1,place-1,place])
        que.append([count+1,place*2,place])

min_route = [K]

for i in range(arr[K]):
    index = min_route[-1]
    min_route.append(route[index])
    index = route[index]

print(arr[K])
while min_route:
    print(min_route.pop(), end = ' ')