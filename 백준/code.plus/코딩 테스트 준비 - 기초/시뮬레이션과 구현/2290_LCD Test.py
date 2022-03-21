n,m = input().split()
n = int(n)
sp4 = " "*(n+2)
sp3col1 = " "*(n+1) + "|"
col1sp3 = "|" + " "*(n+1)
col1sp2col1 = "|" + " "*n + "|"
sp1row2sp1 = " " + "-"*n + " "



string = ["", "", "", "", ""]

zero = [sp1row2sp1, col1sp2col1, sp4, col1sp2col1, sp1row2sp1]
one = [sp4, sp3col1, sp4, sp3col1, sp4]
two = [sp1row2sp1, sp3col1, sp1row2sp1, col1sp3, sp1row2sp1]
three = [sp1row2sp1, sp3col1, sp1row2sp1, sp3col1, sp1row2sp1]
four = [sp4, col1sp2col1, sp1row2sp1, sp3col1, sp4]
five = [sp1row2sp1,col1sp3,sp1row2sp1,sp3col1,sp1row2sp1]
six = [sp1row2sp1,col1sp3,sp1row2sp1,col1sp2col1,sp1row2sp1]
seven = [sp1row2sp1,sp3col1,sp4,sp3col1,sp4]
eight = [sp1row2sp1,col1sp2col1,sp1row2sp1,col1sp2col1,sp1row2sp1]
nine = [sp1row2sp1,col1sp2col1,sp1row2sp1,sp3col1,sp1row2sp1]

nums = [zero,one,two,three,four,five,six,seven,eight,nine]

for i in m:
    x = int(i)
    s = nums[x]
    for j in range(5):
        string[j] += s[j] + " "

print(string[0][:-1])
for _ in range(n):
    print(string[1][:-1])
print(string[2][:-1])
for _ in range(n):
    print(string[3][:-1])
print(string[4][:-1])
