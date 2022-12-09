from math import sqrt
from math import acos
from math import degrees

def find_angle(ab,bc):
    ac=sqrt(ab**2+bc**2)
    mc=ac/2
    bc=bc/2
    the_angle=degrees(acos(bc/mc))
    the_angle=int(round(the_angle))
    print(f"{the_angle}{chr(176)}")
ab=int(input())
bc=int(input())

find_angle(ab,bc)


