x = int(input("insira um numero de 4 digitos "))
a = int(x % 10)
b = int(x / 10) % 10
c = int(x / 100) % 10
d = int(x / 1000) % 10
if a == b == c == d:
    print("todos os digitos sao iguais ")
else:
    print("nao sao iguais")   