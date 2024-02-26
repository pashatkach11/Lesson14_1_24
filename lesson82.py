my_list = [5, 5, 5, 2, 2, 0.5]

def find_unique_value(some_list):
    chislo: float
    for i in range(len(some_list)):
        chislo = some_list[i]
        if some_list.count(some_list[i]) == 1: break
    return chislo

print(find_unique_value(my_list))
