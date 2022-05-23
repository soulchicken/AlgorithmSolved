import sys
from itertools import combinations as com
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    li = [list(map(int,input().split())) for _ in range(n)]
    total_x, total_y = 0, 0
    answer = float('inf')
    
    for i,j in li:
        total_x += i
        total_y += j


    for arr in com(li, n//2):
        sum_x,sum_y = 0, 0
        for x,y in arr:
            sum_x += x
            sum_y += y

        length = (total_x - 2*sum_x)**2 + (total_y - 2*sum_y)**2
        if answer > length:
            answer = length

    print(answer**0.5)