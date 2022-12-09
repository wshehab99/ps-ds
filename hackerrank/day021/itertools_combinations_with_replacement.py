from itertools import combinations_with_replacement
def itertools_combinations_with_replacemen(str_list,k):
    str_list.sort()
    result=list(combinations_with_replacement(str_list,k))
    for item in result:
        print("".join(item))

string=input().split()
itertools_combinations_with_replacemen(list(string[0]),int(string[1]))
