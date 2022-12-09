from collections import deque

def pilling(block):
    for x in reversed(sorted(block)):
        if block[-1]==x:
            block.pop()
        elif block[0]==x:
            block.popleft()
        else:
            print("No")
            break
    else:
        print("Yes")


T=int(input())
for i in range(T):
    n= int(input())
    queue=deque(map(int, input().split()))

    pilling(queue)