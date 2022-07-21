from itertools import combinations


N=int(input())
s=input().split()
k=int(input())
a=list(combinations("".join(s),k))
result=0
for item in a :
    if item.__contains__('a'):
        result+=1
result=round(result/ len(a),3)
print(result)