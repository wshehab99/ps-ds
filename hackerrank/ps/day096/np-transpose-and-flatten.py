import numpy

n, m = [int(x) for x in input().strip().split(' ')]
array = []
for i in range(n) :
    array.append([int(x) for x in input().strip().split(' ')])
array = numpy.array(array)
print(array.transpose())
print(array.flatten())