import re

for _ in range(int(input())):
    text = input()
    text = re.sub("(?<=[ ])\&\&(?=[ ])", "and", text)
    text = re.sub("(?<=[ ])\|\|(?=[ ])", "or", text)
    print(text)
