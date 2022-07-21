from collections import OrderedDict

n=int(input())
ordered=OrderedDict()
words=[]
for i in range(n):
    word=input()
    if word in ordered:
        ordered[word]+=1
    else:
        ordered[word]=1

print(len(ordered))
for key,value in ordered.items():
    print(value,end=" ")