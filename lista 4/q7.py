x = 0

for z in range(1, 201):
    y = 0

    for a in range(1, z + 1):
        if z % a == 0:
            y += 1

    if y == 2:
        x += 1

print(x)