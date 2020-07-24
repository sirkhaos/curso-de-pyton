try:
    a = int(input("dame un numero: "))
    b = int(input("dame otro numero: "))
except ValueError:
    print("ese no es un numero")
else:
    suma = a + b
    print("la suma es " + str(suma))
