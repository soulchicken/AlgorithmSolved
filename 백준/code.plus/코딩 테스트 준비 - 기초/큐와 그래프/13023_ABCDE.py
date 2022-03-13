import sys
input = sys.stdin.readline

N, M = map(int,input().split())
people = [[] for _ in range(N)]
check = [True]*N
stack = []
answer = 0
for _ in range(M):
    a,b = map(int,input().split())
    people[a].append(b)
    people[b].append(a)

def DFS(person,depth):
    global answer
    if answer == 1:
        return
    if depth == 5:
        answer = 1
        return

    check[person] = False
    stack.append(person)
    for x in people[person]:
        if check[x]:
            DFS(x,depth+1)
    stack.append(person)
    check[person] = True


for i in range(N):
    stack.append(i)
    check[i] = False
    DFS(i,1)
    stack.pop()
    check[i] = True
    
print(answer)