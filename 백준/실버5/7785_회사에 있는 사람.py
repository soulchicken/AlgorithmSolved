import sys
input = sys.stdin.readline
company = set()
for _ in range(int(input())):
    name, do = input().split()
    if do == 'enter':
        company.add(name)
    else:
        company.discard(name)
company = list(company)
company.sort(reverse =True)
for people in company:
    print(people)
