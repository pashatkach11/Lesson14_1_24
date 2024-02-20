list_dict = [
    {"name": "John", "age": 15},
    {"name": "Jo", "age": 15},
    {"name": "Jack", "age": 45}
]
print(list_dict)

list_age = []
list_name = []
list_minage = []
list_maxname = []
sum_age = 0

for i in range(len(list_dict)):
    list_age.append(list_dict[i].get("age"))
    list_name.append(len(list_dict[i].get("name")))
    sum_age = sum_age + list_dict[i].get("age")

min_age = min(list_age)
max_name = max(list_name)


for i in range(len(list_dict)):
    if min_age == list_dict[i].get("age"):
        list_minage.append(list_dict[i].get("name"))
    if max_name == len(list_dict[i].get("name")):
        list_maxname.append(list_dict[i].get("name"))


print("Імена наймолодших: ",list_minage)
print("Найдовші імена: ",list_maxname)
print("Середній вік:",sum_age/len(list_dict))

