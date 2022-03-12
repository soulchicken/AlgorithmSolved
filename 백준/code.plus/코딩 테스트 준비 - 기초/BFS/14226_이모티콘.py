from collections import deque
n = int(input())
max_num = 2*n + 1
counts = [[50000]*max_num for _ in range(max_num)]
que = deque()
que.append((0,0,1)) # count, clip, index
while que:
    count,clip,index = que.popleft()
    if 0 < index and index < max_num and counts[index][clip] > count:
        counts[index][clip] = count
        que.append((count + 1,clip, index - 1))
        if counts[index][index] > count:
            que.append((count + 1,index,index))
    if clip != 0 and 0 < index and index + clip < max_num and count + 1 < counts[index+clip][clip]:
        que.append((count + 1, clip, index + clip))
##print(counts)
print(min(counts[n]))