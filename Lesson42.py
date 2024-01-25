my_list = [0, 1, 7, 2, 4, 8]
rezultat = 0

for i in range(0,len(my_list),2):
    rezultat = rezultat + my_list[i]


if my_list != []:
    rezultat = rezultat * my_list[-1]


print(rezultat)