x = int(input("insira um numero (insira 0 para acabar) "))
y = 1
while x != 0:
    if x < 0 or x > 100:
        print("insira um numero positivo e menor que 100")
        x = int(input("insira um numero (insira 0 para acabar) "))
    else:
        while x * y < 100:
            print(x * y)
            y += 1
        x = int(input("insira um numero (insira 0 para acabar) "))
        y = 1 