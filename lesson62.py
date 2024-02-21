my_dict_1 = {1:1, 2:2}
my_dict_2 = {11:11, 2:22}
nov_dict = {}

print(my_dict_1)
print(my_dict_2)

list_keys1 = list(my_dict_1.keys())
list_keys2 = list(my_dict_2.keys())

list_oba = []
list_eu1 = []
dict_eu1 = {}
dict_nov = {}

for i in range(len(list_keys1)):
    if list_keys1[i] in list_keys2:
        list_oba.append(list_keys1[i])
        dict_nov.update({list_keys1[i]: [my_dict_1.get(list_keys1[i]), my_dict_2.get(list_keys1[i])]})
    if list_keys1[i] not in list_keys2:
        list_eu1.append(list_keys1[i])
        dict_eu1.update({list_keys1[i]: my_dict_1.get(list_keys1[i])})
        dict_nov.update({list_keys1[i]: my_dict_1.get(list_keys1[i])})

for i in range(len(list_keys2)):
    if list_keys2[i] not in list_keys1:
        dict_nov.update({list_keys2[i]: my_dict_2.get(list_keys2[i])})


print("Список із ключів, які є в обох словниках:",list_oba)
print("Список із ключів, які є в першому але нема у другому:",list_eu1)
print("Пари {ключ:значення} для ключів, які є в першому, але немає в другому",dict_eu1)
print("Два словники об'єднані за правилом : ", dict_nov)