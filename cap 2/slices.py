numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\n")
print(numeros[1])
print(numeros[0:6])
print(numeros[0:9999999])
print(numeros[5:])
print(numeros[:6])
print(numeros[:])
print(numeros[-6:-3])
print(numeros[:-3])
print(numeros[-6:])

# steps

print(numeros[::2])
print(numeros[::3])
print(numeros[2:8:2])
print(numeros[::-1])
print(numeros[-2:-5:-1])
print(numeros[::2])

# borrado o remplazo

del numeros[0]
print(numeros)
del numeros[0:4]
print(numeros)
del numeros[7:8]
print(numeros)
numeros[1:2] = [12, 13, 15, 16]
print(numeros)
numeros[4:] = [22, 23, 24, 25]
print(numeros)
