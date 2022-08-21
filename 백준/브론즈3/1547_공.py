ball = [0,1,0,0]
for _ in range(int(input())):
    a,b = map(int,input().split())
    ball[a],ball[b] = ball[b],ball[a]
for i in range(4):
    if ball[i]: print(i)
