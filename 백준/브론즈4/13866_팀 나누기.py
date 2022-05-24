from itertools import combinations as com 

li = list(map(int,input().split()))
total = sum(li)
min_num = float('inf')
for a,b in com(li,2):
    x = abs(total - 2*(a+b))
    min_num = min(x,min_num)
print(min_num)
