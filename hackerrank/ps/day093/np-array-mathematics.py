import numpy
n, m = [int(x) for x in input().split()]
array_1=[]
for i in range(n):
    array_1.append([int(x) for x in input().split()])
array_1 = numpy.array(array_1, int)
array_2=[]
for i in range(n):
    array_2.append([int(x) for x in input().split()])
array_2 = numpy.array(array_2, int)
print(numpy.add(array_1, array_2))
print(numpy.subtract(array_1, array_2))
print(numpy.multiply(array_1, array_2))
print(numpy.floor_divide(array_1, array_2))
print(numpy.mod(array_1, array_2))
print(numpy.power(array_1, array_2))