def wrapper(f):
    def fun(l):
        result = []
        for item in l:
            result.append("+91 "+item[-10:-5] + " " + item[-5:])
        f(result)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


