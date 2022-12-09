from collections import OrderedDict
def merge_the_tools(string, k):

    from collections import OrderedDict
    for i in range(0,len(string),k):
        print(''.join(OrderedDict.fromkeys(string[i:i + k])))


string,k=input(),int(input())
merge_the_tools(string,k)