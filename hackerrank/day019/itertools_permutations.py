from itertools import permutations

def itertools_permutations(str_list,k):
    result=list(permutations(str_list,k))
    result.sort()
    for item in result:
        print("".join(item))

string=input().split()
itertools_permutations(list(string[0]),int(string[1]))