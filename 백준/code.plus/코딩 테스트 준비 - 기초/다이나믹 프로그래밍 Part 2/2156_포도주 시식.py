n = int(input())
juice = [int(input()) for _ in range(n)]

if n == 1:
    print(juice[0])


else:
    no_pick = [0]*n
    pick_one = [0]*n
    pick_double = [0]*n
    no_pick[1] = juice[0]
    pick_one[0] = juice[0]
    pick_one[1] = juice[1]
    pick_double[0] = juice[0]
    pick_double[1] = juice[0] + juice[1]

    no_pick_max = juice[0]

    for i in range(2,n):
        no_pick[i] = max(pick_one[i-1], pick_double[i-1],no_pick_max)
        pick_one[i] = juice[i] + no_pick_max
        pick_double[i] = juice[i] + pick_one[i-1]
        if no_pick[i] > no_pick_max:
            no_pick_max = no_pick[i]

    print(max(no_pick[-1], pick_one[-1], pick_double[-1]))
