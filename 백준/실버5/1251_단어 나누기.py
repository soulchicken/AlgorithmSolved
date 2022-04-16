s=input();a=len(s);print(sorted([s[i::-1]+s[j:i:-1]+s[:j:-1] for i in range(a-2) for j in range(i+1,a-1)])[0])
