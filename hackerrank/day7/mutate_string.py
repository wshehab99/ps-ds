from typing import List


def mutate_string(string, position, character):
    string_list=list(string)
    string_list[position]=character
    return "".join(string_list)

s=input()
i,c=input().split()
s_new=mutate_string(s,int (i),c)
print(s_new)