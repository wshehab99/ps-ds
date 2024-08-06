import numpy

array_1 = numpy.array([int(x) for x in input().strip(" ").split()])
array_2 = numpy.array([int(x) for x in input().strip(" ").split()])
print(numpy.inner(array_1,array_2))
print(numpy.outer(array_1,array_2))