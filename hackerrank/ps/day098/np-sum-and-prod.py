import numpy

array = []

n, m = [int(x) for x in input().strip(' ').split()]
for i in range(n):
    array.append([int(x) for x in input().strip(' ').split()[:m]])
sum_array =  numpy.sum(array,axis=0)
print(numpy.prod(sum_array))