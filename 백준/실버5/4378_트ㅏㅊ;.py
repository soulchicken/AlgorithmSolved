# import imp


# s1 = "1234567890-= WERTYUIOP[]\ SDFGHJKL;' XCVBNM,./"
# s2 = '`1234567890- QWERTYUIOP[] ASDFGHJKL; ZXCVBNM,.'
# q = input()
# table = str.maketrans(s1,s2)
# print(q.translate(table))

# while True:
#     try:print(input().translate(str.maketrans("1234567890-=WERTYUIOP[]\SDFGHJKL;'XCVBNM,./",'`1234567890-QWERTYUIOP[]ASDFGHJKL;ZXCVBNM,.')))
#     except:break

import sys;print(sys.stdin.read().translate(str.maketrans("1234567890-=WERTYUIOP[]\SDFGHJKL;'XCVBNM,./",'`1234567890-QWERTYUIOP[]ASDFGHJKL;ZXCVBNM,.')))
    
