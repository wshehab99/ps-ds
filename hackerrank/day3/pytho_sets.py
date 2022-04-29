def average(array):
    arr_set=set(array)
    summ=0
    avg=0
    for item in arr_set:
        summ+=item
    avg=summ/len(arr_set)
    return avg
  

n = int(input())
arr = map(int, input().split())
result = average(arr)
print (result)