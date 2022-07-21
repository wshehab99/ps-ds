from itertools import combinations
def itertools_combinations(str_list,k):
    str_list.sort()
    for i in range(1,k+1):
        result=list(combinations(str_list,i))
        result.sort()
        for item in result:
            print("".join(item))


string=input().split()
itertools_combinations(list(string[0]),int(string[1]))