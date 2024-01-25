my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]


for i in range(len(my_list)):
    if my_list[i] == 0:
        my_list.remove(0)
        my_list.append(0)


print(my_list)