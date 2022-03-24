n = int(input())
num = list(map(int,input().split()))
li = list(map(int,input().split()))

def oper(num1, num2, oper):
    if oper == 0: return num1 + num2
    elif oper == 1: return num1 - num2
    elif oper == 2: return num1 * num2

    if num1 >= 0:
        return num1 // num2
    num1 *= -1
    return (num1 // num2) * -1

answer = [-float('inf'),float('inf')]

def DFS(total, depth):
    if depth == n-1:
        answer[0] = max(answer[0],total)
        answer[1] = min(answer[1],total)
        return
    for i in range(4):
        if li[i] != 0:
            li[i] -= 1
            DFS(oper(total, num[depth+1], i),depth + 1)
            li[i] += 1
    return
DFS(num[0],0)
print(answer[0])
print(answer[1])
