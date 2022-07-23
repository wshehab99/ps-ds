N,X=list(map(int,input().split()))
result=[]
for _ in range(X):
    result.append(list(map(float,input().split())))
nn=[]
for i in zip(*result):
    print(sum(i)/len(i))
