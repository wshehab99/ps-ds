K = int(input())
rooms=list(map(int,input().split()))
rooms=sorted(rooms)
for i in range(len(rooms)):
    if(i!=len(rooms)-1):
        if(rooms[i]!=rooms[i+1] and rooms[i]!=rooms[i-1]):
            print(rooms[i])
            break
    else:
        print(rooms[i])