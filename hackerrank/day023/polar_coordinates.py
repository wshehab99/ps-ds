from cmath import phase
def polar_coordinates(complex_n):
    m=abs(complex_n)
    print(m)
    p=phase(complex_n)
    print(p)

n=complex(input())

polar_coordinates(n)