li = []
while 1:
    try:
        li.extend(list(input().split()))
    except:
        break
total = len(li)
Re = li.count('Re')
print(f'Re {Re} {(Re/total):.2f}')
Pt = li.count('Pt')
print(f'Pt {Pt} {(Pt/total):.2f}')
Cc = li.count('Cc')
print(f'Cc {Cc} {(Cc/total):.2f}')
Ea = li.count('Ea')
print(f'Ea {Ea} {(Ea/total):.2f}')
Tb = li.count('Tb')
print(f'Tb {Tb} {(Tb/total):.2f}')
Cm = li.count('Cm')
print(f'Cm {Cm} {(Cm/total):.2f}')
Ex = li.count('Ex')
print(f'Ex {Ex} {(Ex/total):.2f}')
print(f'Total {total} 1.00')
