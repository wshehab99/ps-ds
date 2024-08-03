def checkCardNumber(number:str):
    # It must contain exactly 16 digits.
    if len(number.replace('-','')) != 16:
        return False
    # It must start with a 4, 5 or 6.
    if number[0]!='4' and number[0]!='5' and number[0]!='6' :
        return False
    # It must only consist of digits (0-9).
    if not number.replace('-',"").isdigit():
        return False
    # It may have digits in groups of 4, separated by one hyphen "-".
    d=0
    for i in range(len(number)):
        if (number[i]=='-' and d!=4):
            return False
        elif (number[i]=='-' and d==4):
            d=0
        else:
            d+=1
    # It must NOT use any other separator like ' ' , '_', etc.
    if(" " in number or "_" in number):
        return False
    #  It must NOT have 4 or more consecutive repeated digits.
    c= 0
    cc=number.replace('-','')
    for i in range(len(cc)-1):
        if cc[i]==cc[i+1]:
            c+=1
        else:
            c=0
        if c==3:
            return False
    #all conditions passed
    return True

for _ in range(int(input())):
    if checkCardNumber(input()):
        print("Valid")
    else:
        print("Invalid")