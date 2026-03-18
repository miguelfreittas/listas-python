s = int(input("inicio do intervalo "))
e = int(input("fim do intervalo "))

for x in range(s, e + 1):
    a = x
    y = 0
    
    while a > 0:
        a //= 10
        y += 1
    
    a = x
    z = 0
    
    while a > 0:
        d = a % 10
        z += d ** y
        a //= 10
    
    if z == x:
        print(x)