a,b,c = map(int,input().split())
def solution(n,m):
    a,b = n,m # a가 b보다 크다
    if a < b:
        a,b = b,a
    while b:
        a, b = b, a % b
    return n*m//a

print(solution(solution(a,b),c))