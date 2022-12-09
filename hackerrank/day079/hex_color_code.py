import re
n = int(input())

for i in range(n):
  s = input()
  
  w = s.split()
  if len(w)>1 and '{' not in w:
    w = re.findall(r'#[a-fA-F0-9]{3,6}', s)
    [print(i) for i in w]