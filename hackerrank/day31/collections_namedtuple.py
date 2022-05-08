from collections import namedtuple
n=int(input())
s=",".join(input().split())
Student=namedtuple('Student',s)
summ=0
for i in range(n):
    student=input().split()
    m=Student(*student)
    summ+=int(m.MARKS)

print(summ/n)
    