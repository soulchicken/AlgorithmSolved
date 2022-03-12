from itertools import permutations as per

n = int(input())
li = list(input().split())
nums = [0,1,2,3,4,5,6,7,8,9]
first = ""
first_flag = True
last = ""
def f(a,b,q):
    if q == ">":
        if a > b: return True
        else: return False
    else:
        if a < b: return True
        else: return False

for pick in per(nums,n+1):
    flag = True
    for i in range(n):
        flag = f(pick[i],pick[i+1],li[i])
        if not flag:
            break
    if flag:
        if first_flag:
            first = pick
            first_flag = False
        last = pick

print(str(last).replace(", ","").replace("(","").replace(")",""))
print(str(first).replace(", ","").replace("(","").replace(")",""))