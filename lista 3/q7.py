x = 1
while x <= 50:
    if x % 4 == 0 and x % 6 == 0:
        print("quadhex")
    elif x % 4 == 0:
        print("quad")
    elif x % 6 == 0:
        print("hex")
    else:
        print(n)
    x += 1