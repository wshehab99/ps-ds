from collections import defaultdict

def def_defaultdict(n,m):
    a=[]
    d=defaultdict(list)
    for i in range(1,n+1):
        d[input()].append(i)
    b=[]
    for i in range(1,m+1):
        key=input()
        if key in d.keys():
            print(" ".join(str(value) for value in d[key]))
        else:
            print(-1)
   


n,m=map(int,input().split())



def_defaultdict(n,m)


