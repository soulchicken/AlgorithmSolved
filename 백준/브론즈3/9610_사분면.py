q1,q2,q3,q4,ax = 0,0,0,0,0
for _ in range(int(input())):
    a,b = map(int,input().split())
    if not a*b: ax += 1
    elif a*b > 0:
        if a > 0: q1 += 1
        else: q3 += 1
    else:
        if a > 0: q4 += 1
        else: q2 += 1
print(f"""Q1: {q1}
Q2: {q2}
Q3: {q3}
Q4: {q4}
AXIS: {ax}""")
