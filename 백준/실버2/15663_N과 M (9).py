import sys
from itertools import permutations as per
input = sys.stdin.readline
N,M = map(int,input().split())
li = sorted(list(map(int,input().split())))
make = []
for i in per(li, M):
    make.append(i)

make.sort()
for i in range(len(make)):
    if i == 0 or make[i-1] != make[i]:
        for n in make[i]:
            print(n,end = ' ')
        print()
