import numpy

n = int(input())
array_1 = []
for _ in range(n):
    array_1.append([int(x) for x in input().strip(" ").split()])

array_1 = numpy.array(array_1)
array_2 = []
for _ in range(n):
    array_2.append([int(x) for x in input().strip(" ").split()])

array_2 = numpy.array(array_2)
c = numpy.dot(array_1,array_2)
print(c)