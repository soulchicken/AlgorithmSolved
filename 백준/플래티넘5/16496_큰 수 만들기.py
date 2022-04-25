n = int(input())
numbers = list(input().split())
for i in range(len(numbers)):
    numbers[i] *= 9
numbers.sort(reverse = True)
answer = ''
for i in range(len(numbers)):
    answer += numbers[i][:len(numbers[i])//9]
if int(answer) == 0:
    print(0)
else: print(answer)
