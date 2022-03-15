import sys
from itertools import combinations_with_replacement as com
input = sys.stdin.readline
N,M = map(int,input().split())
li = set((list(map(int,input().split()))))
li = list(li)
li.sort()
make = []
for i in com(li, M):
    make.append(i)

make.sort()
for i in range(len(make)):
    if i == 0 or make[i-1] != make[i]:
        for n in make[i]:
            print(n,end = ' ')
        print()
