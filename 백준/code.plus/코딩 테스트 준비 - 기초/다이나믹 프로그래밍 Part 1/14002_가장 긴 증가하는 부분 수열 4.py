N = int(input())
li = list(map(int,input().split()))
count = [1]*N
route = [None]*N
max_count = 1
max_index = 0
for i in range(1,N):
    for j in range(i):
        if li[i] > li[j] and count[j] >= count[i]:
            count[i] = count[j]+1
            route[i] = j
    if max_count < count[i]:
        max_count = count[i]
        max_index = i
print(max_count)
stack = []
stack.append(li[max_index])
for i in range(max_count-1):
    max_index = route[max_index]
    stack.append(li[max_index])
while stack:
    print(stack.pop(), end = ' ')
