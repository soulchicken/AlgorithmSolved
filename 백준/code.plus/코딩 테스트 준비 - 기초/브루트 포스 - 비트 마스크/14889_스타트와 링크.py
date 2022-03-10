from itertools import combinations as com
import sys
input = sys.stdin.readline
N = int(input())
arr = [i for i in range(N)]
li = [list(map(int,input().split())) for _ in range(N)]
max_num = 20000
for c in com(arr,N//2):
    starts = c
    links = list(set(arr) - set(starts))
    start = 0
    link = 0
    for two_num in com(starts,2):
        start += li[two_num[0]][two_num[1]]
        start += li[two_num[1]][two_num[0]]

    for two_num in com(links,2):
        link += li[two_num[0]][two_num[1]]
        link += li[two_num[1]][two_num[0]]
    max_num = min(max_num, abs(start - link))
    
print(max_num)
