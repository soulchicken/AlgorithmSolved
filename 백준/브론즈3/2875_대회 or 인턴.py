a,b,c = map(int,input().split())
team = min(a//2,b)
a -= 2*team
b -= team
c -= a+b
while c > 0:
    team -= 1
    c -= 3
print(max(team,0))
    
