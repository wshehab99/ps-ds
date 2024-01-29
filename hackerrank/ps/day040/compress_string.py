from itertools import groupby
def number_of_occurence(s):
    result=[]
    s=groupby(s)
    for key,group in s:
        x=len(list(group))
        result.append((x,int(key)))

    for item in result:
        print(item,end=" ")


s=input()
number_of_occurence(s)