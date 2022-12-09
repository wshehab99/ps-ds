def palindromic_integer(n):
    n=str(n)
    return n==n[::-1]

n=int(input())
num=list(map(int,input().split()[:n]))
print(all(item>0 for item in num) and any(palindromic_integer(number) for number in num) )
