from itertools import permutations as per
n = int(input())
li = [i+1 for i in range(n)]
for ss in per(li,n):
    print(str(ss).replace("(","").replace(")","").replace(",",""))