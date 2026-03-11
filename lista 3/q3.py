x = int(input("insira um numero, (insira -1 para acabar) "))
y = 0
z = 0
while x != -1:
    y += x
    z += 1
    x = int(input("insira um numero, (insira -1 para acabar) "))
if z == 0:
    print("nenhum numero diferente de -1 foi inserido")
else:
    print(f"a media e {y / z}")

