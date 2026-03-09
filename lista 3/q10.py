x = int(input("Digite o início do intervalo: "))
y = int(input("Digite o fim do intervalo: "))

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