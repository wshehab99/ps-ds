def split_and_join(line):
    # write your code here
    words=line.split()
    return "-".join(words)

result = split_and_join(input())
print (result)