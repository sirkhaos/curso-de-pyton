manzanas = 10

while manzanas > 0:
    print("me estoy comiendo una manzana " + str(manzanas))
    manzanas -= 1
print("me quede sin manzanas")

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\n")

for num in lista_numeros:
    if num > 5:
        break
    print(num)

print("\n")

for num in lista_numeros:
    if num == 5:
        continue
    print(num)

print("\n")

vocales = list("aeiou")

for let in vocales:
    print(let.upper())
