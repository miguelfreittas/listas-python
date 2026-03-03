x = int(input("insira um numero de 4 digitos "))
a = int(x / 1000)
b = int(x / 100) % 10
c = int(x / 10) % 10 
d = int(x % 10)
if a == d and b == c:
    print("o numero e espelhado") 
else:
    print("o numero nao e espelhado") 
