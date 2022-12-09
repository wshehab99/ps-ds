import re
n=int(input())
for _ in range(n):
    t=input()
    r=re.match(r'^[+-]?[0-9]*\.[0-9]+$',t)
    print(bool(r))
