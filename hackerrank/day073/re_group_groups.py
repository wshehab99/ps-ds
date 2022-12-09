import re
s=input()
r=re.findall(r"([a-zA-Z0-9])\1+",s)
if len(r)==0:
    print(-1)
else:
    print(r[0])
