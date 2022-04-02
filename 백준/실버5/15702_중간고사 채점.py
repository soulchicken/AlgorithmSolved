import sys
n,m = map(int,input().split())
score = list(map(int,input().split()))
answer_person = 1000
answer_total = -1000
for i in range(m):
    person = list(input().split())
    total = 0
    for j in range(n):
        if person[j+1] == 'O':
            total += score[j]
    if total > answer_total:
        answer_total = total
        answer_person = int(person[0])
    elif total == answer_total and answer_person > int(person[0]):
        answer_person = int(person[0])
print(answer_person,answer_total)
