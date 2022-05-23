school = list(map(int,input().split()))
name = ['Soongsil','Korea','Hanyang']
if sum(school) >= 100: print('OK')
else: print(name[school.index(min(school))])