first_chislo = int(input("Введіть перше число: "))
second_chislo = int(input("Введіть друге число: "))
diya = input("Введіть дію: ")

if diya == "+":
    result = first_chislo + second_chislo

if diya == "-":
    result = first_chislo - second_chislo

if diya == "*":
    result = first_chislo * second_chislo

if diya == "/":
    if second_chislo == 0:
        result = "Дільник не може бути 0"
    else:
        result = first_chislo / second_chislo

print(result)
