import numpy

array = numpy.array([float(x) for x in input().strip(' ').split()])
numpy.set_printoptions(legacy='1.13')
print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))