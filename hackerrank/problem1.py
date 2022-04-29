N = int(input())
numbers=[]
for i in range(N):
    x=input().split()
    if(x[0]=='print'):
        print(numbers)
    elif(x[0]=='insert'):
        numbers.insert(int(x[1]),int(x[2]))
    elif(x[0]=='append'):
        numbers.append(int(x[1]))
    elif(x[0]=='remove'):
        numbers.remove(int(x[1]))
        
    elif(x[0]=='pop'):
        numbers.pop()
    elif(x[0]=='sort'):
        numbers.sort()
    else:
        numbers.reverse()