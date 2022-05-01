
def print_formatted(number):
    result=[]
    for i in range(1,number+1):
        result.append(str(i))
        result.append(oct(i).replace("0o",""))
        result.append(hex(i).replace("0x","").capitalize())
        result.append(bin(i).replace("0b",""))
        for n in result:
            print(f"{' '*(6-len(n))}{n}",end="",)
        print()
        result=[]
        
       

if __name__=="__main__":
    n=int(input())
    print_formatted(n)
    #binary