from itertools import product
k,m=map(int,input().split())
list_of=[]
for _ in range(k):
    i=list(map(int,input().split()))
    list_of.append(i[1:])
list_of=list(product(*list_of))
results=[]
for i in list_of:
    r=sum([pow(a,2) for a in i])
    results.append(r%m)
result=max(results)
print(result)




