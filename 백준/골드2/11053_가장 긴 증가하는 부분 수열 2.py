from bisect import bisect_left as bile
input()
li = list(map(int,input().split()))
arr = [li[0]]
for i in range(len(li)):
    if li[i] > arr[-1]:arr.append(li[i])
    else: arr[bile(arr,li[i])] = li[i]
print(len(arr))
