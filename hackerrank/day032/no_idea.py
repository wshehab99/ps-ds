n,m=map(int,input().split())
array=list(map(int,input().split()))
a=set(list(map(int,input().split())))
b=set(list(map(int,input().split())))
happiness=0
for item in array:
    if item in a:
        happiness+=1
    if item in b:
        happiness-=1
print(happiness)
