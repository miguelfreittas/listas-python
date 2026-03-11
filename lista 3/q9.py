x = int(input("insira um numero "))

y = 0
z = 1

while z < x:
    if x % z == 0:
        y += z
    z += 1

if y == x:
    print("numero perfeito")

else:
    print("nao e um numero perfeito")
    