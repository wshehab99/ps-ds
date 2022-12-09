from collections import OrderedDict
n=int(input())
items=OrderedDict()
for i in range(n):
    s=input().split()
    if " ".join(s[:-1]) in items.keys():
        items[" ".join(s[:-1])]+=int(s[-1])
    else:
        items[" ".join(s[:-1])]=int(s[-1])

for key,value in items.items():
    print(key,value)