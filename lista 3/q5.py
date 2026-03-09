x = int(input("insira um numero "))
y = 1
z = x

while z >= 1:
    y = y * z
    z -= 1
print(f"fatorial de {x} é {y}")