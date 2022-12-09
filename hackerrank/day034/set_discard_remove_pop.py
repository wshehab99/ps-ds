n=int(input())
s=set(map(int,input().split()))
no_commad=int(input())
for i in range(no_commad):
    comand=input().split()
    if comand[0]=="remove":
        s.remove(int(comand[1]))
    elif comand[0]=="discard":
        s.discard(int(comand[1]))
    elif comand[0]=="pop":
        s.pop()

print(sum(s))