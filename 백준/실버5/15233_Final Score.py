import sys
input = sys.stdin.readline
a,b,g = map(int,input().split())
A = set(input().split())
B = set(input().split())
G = list(input().split())
a_num, b_num = 0, 0
for i in G:
    if i in A: a_num += 1
    if i in B: b_num += 1
if a_num > b_num:
    print("A")
elif a_num < b_num:
    print("B")
else:
    print("TIE")