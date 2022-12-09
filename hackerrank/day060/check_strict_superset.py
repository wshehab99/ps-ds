A=set(input().split())
result=True
for _ in range(int(input())):
    b=set(input().split())
    result=result and A.issuperset(b)
print(result)