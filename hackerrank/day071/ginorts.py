s=input()
s=sorted(s,key=lambda x:(x.isdigit(),x.isupper(),x in "02468",x))
print(*s,sep="")