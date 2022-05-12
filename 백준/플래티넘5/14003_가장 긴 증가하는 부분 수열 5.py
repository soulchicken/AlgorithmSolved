import bisect
n = int(input())
li = list(map(int,input().split()))
arr = []
index = []
for i in range(n):
    if not arr or li[i] > arr[-1]:
        arr.append(li[i])
        index.append((len(arr) - 1, li[i]))
        
    else:
        a = bisect.bisect_left(arr,li[i])
        arr[a] = li[i]
        index.append((a,li[i]))


count = len(arr)
print(count)
count -= 1
stack = []
while index:
    idx, val = index.pop()
    if idx == count:
        stack.append(val)
        count -= 1

while stack:
    print(stack.pop(),end = ' ')
