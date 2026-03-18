x = int(input("insira um numero  "))
y = 0

for z in range (0, x+1):
    if z % 3 == 0:
        y = y + z
print(y)
