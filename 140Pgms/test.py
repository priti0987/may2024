def remove_duplicate_ids(ids_list):
    mylist_1 = set(ids_list)
    N = len(mylist_1)
    '''
    INPUTS:
        ids_list: A sorted Python list in increasing order.
    OUTPUT:
        A tuple with the number of unique elements N and the updated ids_list
        output = (N, ids_list)
    '''
    return N, mylist_1


mylist = [1, 5, 6, 9, 9, 6, 5, 2, 8]
myset = set(mylist)
myset = list(myset)
print(myset)
print(len(myset))
# print(sorted(mylist))
