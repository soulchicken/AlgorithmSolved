n = int(input())
li = list(map(int,input().split()))
answer = []

for i in range(n):
    answer.insert(li[i],i+1)
answer = answer[::-1]
for i in answer:
    print(i,end=' ')
