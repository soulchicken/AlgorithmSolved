li = list(input().split())
people = ['A','B','C']
one = li.count('1')
zero = li.count('0')
if one == 1:
    print(people[li.index('1')])
elif zero == 1:
    print(people[li.index('0')])
else:
    print('*')
