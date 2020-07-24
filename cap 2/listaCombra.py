# agregar item
# remover item
# ver item

articulos = list()


def addItem(nombre):
    articulos.append(nombre)
    print("\n" + nombre + " a sido agregado a la lista \n")


def delItem(index):
    del articulos[index]


def ver():
    print("----- lista de compra------")
    for item in articulos:
        print(articulos.index(item), end=" - ")
        print(item)
    print("---------------------------")


while True:
    print("estas son las operaciones que puedes realisar \n\n 1.- agregar \n 2.- remover \n 3.- listar \n 4.- salir \n")
    opt = int(input(":"))


    if opt == 1:
        it = input("\n ingresa el item: ")
        addItem(it)
    elif opt == 2:
        ind = int(input("\ningresa el indice a borrar: "))
        delItem(ind)
    elif opt == 3:
        ver()
    elif opt == 4:
        print("\nchiao")
        break
    else:
        pass
