n=int(input())
N=list(map(int,input().split()[:n]))

b=int(input())
B=list(map(int,input().split()[:b]))
print(len(set(N).intersection(set(B))))