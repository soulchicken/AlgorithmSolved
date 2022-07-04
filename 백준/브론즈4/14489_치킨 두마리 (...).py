money = sum(map(int,input().split()))
chicken = 2*int(input())
if money >= chicken:
    print(money - chicken)
else:
    print(money)
