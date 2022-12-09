

def exceptions_handling():
    try:
        a,b=map(int,input().split())
        x=a//b
        print((x))

    except ZeroDivisionError as e:
    
        print(f"Error Code: {e}")

    except ValueError as e:
        print(f"Error Code: {e}")



n=int(input())
for i in range(n):
    
    

    exceptions_handling()