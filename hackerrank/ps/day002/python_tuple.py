n = int(input())
integer_list = map(int, input().split())
i=tuple(integer_list)
print(hash(i))