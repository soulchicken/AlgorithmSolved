from collections import deque
n = int(input())
counts = [float('inf')]*(n+1)
prevs = [float('inf')]*(n+1)
que = deque()
que.append((0,1,1)) # count,place,prev
while que:
    count,place,prev = que.popleft()
    if 0 <= place and place < n+1 and count < counts[place]:
        counts[place] = count
        prevs[place] = prev

        que.append((count+1,place*2,place))
        que.append((count+1,place*3,place))
        que.append((count+1,place+1,place))

route = [n]
while route[-1] != 1:
    index = route[-1]
    index = prevs[index]
    route.append(index)
    
    
print(counts[n])
for i in route:
    print(i, end = ' ')