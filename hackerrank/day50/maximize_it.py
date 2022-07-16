from itertools import product
def max_it(k,m):
    list_of=[]
    for _ in range(k):
        i=list(map(int,input().split()))
        list_of.append(i)
    list_of=list(product(*list_of))
    results=[]
    for i in list_of:
        r=sum([a**2 for a in i])
        r%=m
        results.append(r)
    result=max(results)
    print(result)
K,M=map(int,input().split())
print("I Love python")
max_it(K,M)



