prosto_list = [10.2, -2.2, 0, 1.1, 0.5]

def difference(my_list):
    if my_list == []:
        return 0
    return round(max(my_list) - min(my_list), 2)
print(difference(prosto_list))
print("OK")