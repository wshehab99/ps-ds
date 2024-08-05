import numpy



n, m, p = [int(x) for x in input().split()]
array_1 =[]
for i in range(n):
    array_1.append([int(x) for x in input().split()])
    
array_2 =[]
for i in range(m):
    array_2.append([int(x) for x in input().split()])

concatenate_array = numpy.concatenate((numpy.array(array_1), numpy.array(array_2)))
print(concatenate_array)