tupla1 = (1, 2, 3, 4)
tupla2 = 1, 2, 3, 4
tupla3 = (1)  # no es una tupla
tupla3 = (1,)
tupla4 = (1, "aldo", [0, 1, 2])
print(tupla4)
tupla4[2][2] = 3
print(tupla4)
tupla4[2][2:] = [3, 5]
print(tupla4)
