import sys
input = sys.stdin.readline

n,s = map(int,input().split())
li = list(map(int,input().split()))

left_num = n // 2
right_num = n - left_num

left_bit = [0]*(1<<left_num)
right_bit = [0]*(1<<right_num)

for i in range(1<<left_num):
    for j in range(left_num):
        if i & 1 << j != 0:
            left_bit[i] +=  li[j]

for i in range(1<<right_num):
    for j in range(right_num):
        if i & 1 << j != 0:
            right_bit[i] +=  li[j+left_num]

left_bit.sort()
right_bit.sort(reverse = True)
left = 0
max_left = (1 << left_num)
right = 0
max_right = (1 << right_num)

count = 0
while left < max_left and right < max_right:
    if s == left_bit[left] + right_bit[right]:
        left_count = 1
        right_count = 1
        left += 1
        right += 1
        while left < max_left and left_bit[left] == left_bit[left-1]:
            left_count += 1
            left += 1
        while right < max_right and right_bit[right] == right_bit[right-1]:
            right_count += 1
            right += 1
        count += left_count * right_count
    elif s < left_bit[left] + right_bit[right]:
        right += 1
    else:
        left += 1

if s == 0:
    count -= 1
print(count)
