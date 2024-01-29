
bool_repeat = True

while bool_repeat:
    first_chislo = int(input("Введіть перше число: "))
    second_chislo = int(input("Введіть друге число: "))
    diya = input("Введіть дію: ")
    if diya == "+":
        result = first_chislo + second_chislo

    elif diya == "-":
        result = first_chislo - second_chislo

    elif diya == "*":
        result = first_chislo * second_chislo

    elif diya == "/":
        if second_chislo == 0:
            result = "Дільник не може бути 0"
        else:
            result = first_chislo / second_chislo

    print(result)
    print("Для повтору натисніть y! Для виходу - будь що")
    prap = input()

    if prap !="y" :
        bool_repeat = False
