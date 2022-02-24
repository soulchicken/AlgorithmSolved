n = int(input())
li = [input().rstrip() for _ in range(n)]
if li == sorted(li):print("INCREASING")
elif li == sorted(li)[::-1]:print("DECREASING")
else:print("NEITHER")
