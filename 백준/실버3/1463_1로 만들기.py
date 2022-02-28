n = int(input())
li = [0, 0]
l = 1
while l != n:
    l += 1
    li.append(li[-1] + 1)
    if l % 2 == 0 and li[l // 2] + 1 < li[-1]:
        li[-1] = li[l // 2] + 1
    if l % 3 == 0 and li[l // 3] + 1 < li[-1]:
        li[-1] = li[l // 3] + 1
print(li[n])
