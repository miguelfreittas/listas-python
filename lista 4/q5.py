x = int(input("insira um numero: "))
y = 0

for z in range (1, x):
    if x % z == 0:
        y += z

if y == x:
    print("numero perfeito")
else:
    print("nao e perfeito")