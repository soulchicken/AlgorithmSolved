from itertools import combinations as com
flag = False
while 1:
    lotto = list(map(int,input().split()))
    if lotto[0] == 0:
        break
    if flag:
        print()
    n = lotto.pop(0)
    for pick in com(lotto,6):
        print(str(pick).replace(",","").replace("(","").replace(")",""))

    flag = True