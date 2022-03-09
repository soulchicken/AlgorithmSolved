n = int(input())
s = input().strip()
if n < 26:
    print(s)
elif "." not in s[12:-12]:
    print(s[:11]+"..."+s[-11:])
else:
    print(s[:9]+"......"+s[-10:])
