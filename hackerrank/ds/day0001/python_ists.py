def reverseArray(a):
    result=[]
    for i in range(len(a)-1,-1,-1):
        result.append(a[i])
    return result;