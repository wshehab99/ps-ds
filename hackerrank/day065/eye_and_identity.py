import numpy
numpy.set_printoptions(legacy='1.13')
inpu=list(map(int,input().split()))
N,M=inpu[0],inpu[1]
print(numpy.eye(N,M))