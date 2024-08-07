import numpy

n = int(input())

array= []
for _ in range(n):
    array.append([float(x) for x in input().strip(" ").split()[:n]])
array = numpy.array(array)

print(round(numpy.linalg.det(array),2))