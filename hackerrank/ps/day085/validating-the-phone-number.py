import re
def validateNumber(number):
    
    if(re.match(r"[7-9]\d{9}$",number)):
        return "YES"
    return "NO"
    


for number in range(int(input())):
    print(validateNumber(input()))
