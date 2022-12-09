num=int(input())
A=set(map(int,input().split()[:num]))
n=int(input())
for i in range(n):
    op=input().split()
    B= set(map(int,input().split()[:int(op[1])]))
    if(op[0]=="update"):
        A.update(B)
    elif op[0]=="intersection_update":
        A.intersection_update(B)
    elif op[0]=="difference_update":
        A.difference_update(B)
    elif op[0]=="symmetric_difference_update":
        A.symmetric_difference_update(B)
print(sum(A))