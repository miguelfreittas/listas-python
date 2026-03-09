x = int(input("insira um numero "))

y = ""

while x > 0:
    z = x % 2
    y = str(z) + y
    x = x // 2

print(f"binario de {x} é: {y}")