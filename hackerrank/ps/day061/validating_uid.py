import re
for _ in range(int(input())):
    uid=input()
    if uid.isalnum() and len(uid)==10:
        if re.search(r'(.*[A-Z]){2,}',uid) and re.search(r'(.*[0-9]){3,}',uid):
            if re.search(r'.*(.).*\1+.*',uid):
                print("Invalid")
            else:
                print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")