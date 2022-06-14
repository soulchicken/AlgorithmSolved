n = int(input())
li = list(map(int,input().split()))
arr = [0]*n
arr[0] = li[0]
for i in range(1,n):
    arr[i] = arr[i-1] + li[i]
arr = [0] + arr
for _ in range(int(input())):
    a,b = map(int,input().split())
    print(arr[b+1] - arr[a])
