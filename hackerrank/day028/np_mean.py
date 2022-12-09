import numpy as np
def np_mean_var_std(l):
    my_array=np.array(l)
    print(np.mean(my_array,axis=1))
    print(np.var(my_array,axis=0))
    print(round(np.std(my_array,axis=None),11))

n,m=map(int,input().split())
l=[]

for i in range(n):
    
    a=list(map(int,input().split()))
    l.append(a)
   

np_mean_var_std(l)