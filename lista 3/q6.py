import random

x = random.randint(10,50)
y = int(input("advinhe um numero de 10 a 50 "))

if y >= 10 and y <= 50:
    while y != x:
        
        if y > x:
            print("maior que o numero")
        
        elif y < x:
            print("menor que o numero")
        y = int(input("advinhe um numero de 10 a 50 "))
    
    print("voce acertou o numero")

else:
    print("numero < 10 ou numero > 50")