def wrap(string, max_width):
    result=[]
    sub_string=''
    current_index=0
    for i in range(len(string)//max_width):
        sub_string=string[current_index:current_index+max_width]
        result.append(sub_string)
        current_index+=max_width
    if(len(string)%max_width!=0):
        sub_string=string[current_index:]
        result.append(sub_string)
    return "\n".join(result)

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)