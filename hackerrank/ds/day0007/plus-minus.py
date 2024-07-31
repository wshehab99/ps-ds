import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive = []
    negitive=[]
    zeroes=[]
    for number in arr:
        if number >0:
            positive.append(number)
        elif number<0 :
            negitive.append(number)
        else:
            zeroes.append(number)
    length = len(arr)
    printValue(len(positive)/length)
    printValue(len(negitive)/length)
    printValue(len(zeroes)/length)

def printValue(number):
    return print("{:.6f}".format(number))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
