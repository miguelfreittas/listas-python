x = int(input("insira um numero inteiro positivo: "))
y = 0

for z in range(1, x):
    if z % 4 == 0 or z % 6 == 0:
        y += z

print(f"resultado e {y}")