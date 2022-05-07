from itertools import *;n=int(input());
for d,e,h,l,o,r,w in permutations(range(10),7):
    if n==10000*(h+w)+1000*(e+o)+100*r + 120*l+o+d and h and w:
        print(f'  {h}{e}{l}{l}{o}\n+ {w}{o}{r}{l}{d}\n-------\n' + '{0:>7}'.format(n));break
else:print('No Answer')
