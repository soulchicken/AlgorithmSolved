a = input()
n = int('0x'+a,16)
for i in range(1,16):
    print(a,'*',format(i,'X'),'=',format(n*i,'X'),sep='')
