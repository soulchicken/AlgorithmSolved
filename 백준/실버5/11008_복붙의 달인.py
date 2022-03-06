for _ in range(int(input())):
    s, p = input().split()
    sn = len(s)
    pn = len(p)
    s = s.replace(p,"")
    print((sn-len(s))//pn+len(s))
