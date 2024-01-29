import re
s=input()
m=re.findall(r'(?<=[bcdfghjklmnpqrstvwxyz])([aeiou]{2,})(?=[bcdfghjklmnpqrstvwxyz])',s,re.IGNORECASE)
if len(m)>0:
    print(*m,sep='\n')
else :
    print(-1)