import numpy

n, m  = [int(x) for x in input().strip(" ").split()]
array = []

for _ in range(n):
    array.append([int(x) for x in input().strip(' ').split()[:m]])

array = numpy.array(array)
array = numpy.min(array,axis=1)
print(numpy.max(array))