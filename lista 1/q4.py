a = int(input("que horas e? (0 a 23)"))
b = int(input("quantas horas ate o alarme tocar? "))

x = (a+b) % 24
print(x)