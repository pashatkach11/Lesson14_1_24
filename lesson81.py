my_list = [9, 9, 9]

def add_one(some_list):
    my_str = ""
    itog_list = []
    for i in range(len(some_list)):
        my_str = my_str + str(some_list[i])
    my_str = str(int(my_str) + 1)
    for i in range(len(my_str)):
        itog_list.append(my_str[i])
    return itog_list

print(add_one(my_list))
