no_m=int(input())
m=set(map(int,input().split()))
no_n=int(input())
n=set(map(int,input().split()))

result=m.union(n).difference(m.intersection(n))
result=sorted(result)
for i in result:
    print(i)
