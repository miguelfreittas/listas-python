x = int(input("insira o inicio do intervalo "))
y = int(input("insira o fim do intervalo "))

z = x

while z <= y:
    a = 0
    b = 1

    while b < z:
        if z % b == 0:
            a += b
        b += 1

    if a == z:
        print(z, "é um número perfeito")

    z += 1