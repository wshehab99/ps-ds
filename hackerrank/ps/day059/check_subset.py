T=int(input())
for _ in range(T):
    a=int(input())
    A=set(map(int,input().split()[:a]))
    b=int(input())
    B=set(map(int,input().split()[:b]))
    print(A.issubset(B))