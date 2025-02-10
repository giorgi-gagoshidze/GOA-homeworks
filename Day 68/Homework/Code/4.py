def append_items(om, it):
    om.extend(it)
    return om
my_list = [1, 2, 3]
new_items = [4, 5, 6]
print(append_items(my_list, new_items)) 
