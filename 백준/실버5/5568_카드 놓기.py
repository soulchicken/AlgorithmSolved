n = int(input())
k = int(input())
li = list(input() for i in range(n))
st = set()
s = []
check = [True]*n
def DFS(depth,k,n):
    if depth == k:
        st.add(''.join(s))
        return
    for i in range(n):
        if check[i]:
            s.append(li[i])
            check[i] = False
            DFS(depth + 1,k,n)
            s.pop()
            check[i] = True
DFS(0,k,n)
print(st)
print(len(st))
