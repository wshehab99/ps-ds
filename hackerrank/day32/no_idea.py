n,m=map(int,input().split())
array=list(map(int,input().split()))
a=set(list(map(int,input().split())))
b=set(list(map(int,input().split())))
h=0
for item in array:
    if item in a:
        h+=1
    if item in b:
        h-=1
print(h)
