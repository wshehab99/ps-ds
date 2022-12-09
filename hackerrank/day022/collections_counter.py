from collections import Counter
def collections_counter(list_of_sizes,number_of_custmer):
    sizes_collections=Counter( list_of_sizes)
    earned_money=0
    for i in range(number_of_custmer):

        size_with_value=input().split()
        key=int(size_with_value[0])
        if key in sizes_collections.keys():
            if sizes_collections[key]>0:
                earned_money+=int(size_with_value[1])
                sizes_collections[int(size_with_value[0])]=sizes_collections[key]-1

    return earned_money


n=int(input())
number_of_sizes=list(input().split())
for i in range(n):
    number_of_sizes[i]=int(number_of_sizes[i])

number_of_custmer=int(input())




            
earned_money=collections_counter(number_of_sizes,number_of_custmer)


print(earned_money)

