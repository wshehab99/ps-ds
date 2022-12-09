from itertools import product
def itertools_product(a,b):
    c=list(product(a,b))
    for item in c:
        print(item,end=" ")

a=input().split()
b=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
for i in range(len(b)):
    b[i]=int(b[i])
itertools_product(a,b)