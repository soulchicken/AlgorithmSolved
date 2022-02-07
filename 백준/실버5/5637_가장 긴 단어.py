import sys
input = sys.stdin.readline
li = []
while True:
    li.extend(input().split())
    if li[-1] == 'E-N-D':
        break
li2 = []
for i in li:
    s = ''
    for x in i:
        if x.isalpha() or x == '-':
            s += x
    li2.append(s)

length = 0
index = 0
for i in range(len(li2)-1):
    if len(li2[i]) > length:
        length = len(li2[i])
        index = i
print(li2[index].lower())
