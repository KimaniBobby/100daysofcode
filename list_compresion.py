a = [1, 2, 3, 4, 5]
b = [3, 5, 6]
def difference(a, b):
    b_set = set(b)# Convert list b into a set for faster membership checking.

    new_list = [x for x in a if x not in b_set]
#Create a new list called newlist using a list comprehension.
# The list comprehension iterates through each element x in list a and includes it in the newlist only if it's not present in the set b_set. 
# This effectively removes the elements from a that are present in b, resulting in the difference between the two lists.

    print(new_list)

difference(a,b)