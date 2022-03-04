n = int(input())
x = int(input())
li = [0,1,2,3,4,5,6,7,8,9]
count = [abs(n - 100)]

if x != 0:
    li2 = list(map(int,input().split()))
    li2.sort(reverse = True)
    for i in li2:
        li.pop(i)
        
def DFS(depth,total):
    if depth != 0 and count[0] > abs(total - n) + len(str(total)):
            count[0] = abs(total - n) + len(str(total))    
    if depth == 6:
        return
    for i in li:
        DFS(depth + 1, total*10 + i)
DFS(0,0)
print(count[0])
