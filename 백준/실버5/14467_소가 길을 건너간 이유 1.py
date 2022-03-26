import sys
input = sys.stdin.readline
n = int(input())
malang = [None]*11
count = 0
for i in range(n):
    cow, location = map(int,input().split())
    if malang[cow] == None:
        malang[cow] = location
    elif malang[cow] != location:
        count += 1
        malang[cow] = location
print(count)
