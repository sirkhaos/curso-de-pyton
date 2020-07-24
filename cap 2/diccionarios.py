dic1 = {"pablo": 9, "aldo": 10, "juan": 6, "maritsa": 7}
print(dic1)
print(dic1["aldo"])
dic1["casandra"] = "nueve"
print(dic1)

# Metodo para crear diccionarios
dic2 = dict([["pepe", 7], ["maria", 4]])
print(dic2)

print("\n")

# agregar borrar actualizar

dias = {"lunes": 9, "martes": 10, "miercoles": 11}
print(dias)
dias["jueves"] = 12
print(dias)
del dias["lunes"]
print(dias)
dias.update({"viernes": 13, "sabado": 16})
print(dias)
dias.update({"sabado": 14, "domingo": 15})
print(dias)

print("\n")

# recorriendo el diccionario

for dia in dias:
    print(dia)  # devuelve las llaves

for dia in dias:
    print(dias[dia])  # devuelve valor de cada llave

for key in dias.keys():
    print(key)  # devuelve las llaves

for value in dias.values():
    print(value)  # devuelve valor de cada llave

for item in dias.items():
    print(item)  # devuelve cada elemento del diccionario (key,value)

fe = {"al": [1, 2], "bl": [2, 2]}
for item in fe.items():
    print(item)
