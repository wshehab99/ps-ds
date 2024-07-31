import email.utils
import re
def validateEamil(emailCheck):
    mail = email.utils.parseaddr(emailCheck)
    if re.match(r'[\w\.-]+@[\w\.-]+',mail[1]):
        print( email.utils.formataddr(mail))
    
    


for _ in range(int(input())):
    validateEamil(input())


