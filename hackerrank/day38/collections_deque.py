from collections import deque
def op_deque(op ):
    
    if(op[0]==("append")):
        d.append(op[1])
    elif(op[0]=="appendleft"):
        d.appendleft(op[1])
    elif(op[0]=="clear"):
        d.clear()
    elif(op[0]=="extend"):
        d.extend(op[1])
    elif(op[0]=="extendleft"):
        d.extendleft(op[1])
    elif(op[0]=="pop"):
        d.pop()
    elif(op[0]=="popleft"):
        d.popleft()
    elif(op[0]=="remove"):
        d.remove(op[1])
    elif(op[0]=="reverse"):
        d.reverse()

    elif(op[0]=="rotate"):
        d.rotate(op[1])

    elif(op[0]=="count"):
        d.count(op[1])

   

n = int (input())
d=deque()
for i in range(n):
    x=input().split()
    op_deque(x)
d=list(d)
print(" ".join(d))
