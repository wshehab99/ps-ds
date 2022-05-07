from configparser import InterpolationError
from msilib.schema import Error


def exceptions_handling(a,b):
    try:
        x=a/b

    except ZeroDivisionError as e:
        print(f"Error Code: {e.args}")
    except ValueError as e:
        print(f"Error Code: {e.args}")



n=int(input())
for i in range(n):
    
    a,b=map(int,input().split())

    exceptions_handling(a,b)