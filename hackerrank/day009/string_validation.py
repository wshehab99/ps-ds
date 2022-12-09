from unittest import result


s=input()

#alphanumeric characters.
result=False
for letter in s:
    if letter.isalnum():
        result=True
        break
print(result)

#alphabetical characters.
result=False
for letter in s:
    if letter.isalpha():
        result=True
        break
print(result)

#digits.
result=False
for letter in s:
    if letter.isdigit():
        result=True
        break
print(result)

()
# lowercase
result=False
for letter in s:
    if letter.islower():
        result=True
        break
print(result)
#uppercase
result=False
for letter in s:
    if letter.isupper():
        result=True
        break
print(result)