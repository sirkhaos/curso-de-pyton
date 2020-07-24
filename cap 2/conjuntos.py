# * obtener los set del user, los llamos a y b
# * bebemos hacer la funcion de union
# * bebemos hacer la funcion de interceccion
#  bebemos hacer la funcion de diferencia
#  bebemos hacer la funcion de diferencia simetrica




def interface():
    print("________________________________")
    print("            menu")
    print("--------------------------------")
    print("1 - union\n"
          "2 - interceccion\n"
          "3 - diferencia\n"
          "4 - diferencia cimetrica\n"
          "5 - ver intruciones\n"
          "6 - cambiar conjunto\n"
          "7 - salir\n"
          "--------------------------------\n")

def union(a,b):
    print(a.union(b)) #o podiria ser print(a|b)

def interceccion(a,b):
    print(a.intersection(b)) #o podiria ser print(a&b)

def diferencia(a,b):
    tip = input("elige la diferencia a realisar\n"
                "a. a-b\n"
                "b. b-a\n"
                ":")
    if tip == "a":
        print(a.difference(b))#o podiria ser print(a-b)
    elif tip == "b":
        print(b.difference(a))  # o podiria ser print(b-a)

    else:
        diferencia(a, b)

def newConjunto():
    return set(input("conjunto b: ").split())

def diferenciaCimetrica(a,b):
    print(a.symmetric_difference(b)) #o podiria ser print(a^b)

def calculadoraDeConjuntos():
    print("bienvenidos a los conjuntos")
    print("introduce los conjuntos separados por espacio ")
    print("ejemplo 1 3 5 8 0 2")

    conjuntoA=set(input("conjunto a: ").split())
    conjuntoB=set(input("conjunto b: ").split())

    print(conjuntoA)
    print(conjuntoB)

    opt=None
    interface()
    while opt!=7:
        try:
            opt=int(input(": "))
        except ValueError:
            print("solo se aceptan numeros")
            opt=None
        if opt==1:
            union(conjuntoA,conjuntoB)
        elif opt==2:
            interceccion(conjuntoA,conjuntoB)
        elif opt==3:
            diferencia(conjuntoA, conjuntoB)
        elif opt==4:
            diferenciaCimetrica(conjuntoA,conjuntoB)
        elif opt==5:
            interface()
        elif opt==6:
            tip = input("que conjunto quieres cambiar a o b: ")
            if tip == "a":
                conjuntoA = newConjunto()
            elif tip == "b":
                conjuntoB = newConjunto()
            else:
                print("opcion no valida")
        elif opt==7:
            print("que tengas un buen dia")
        else:
            print("opcion no valida")

calculadoraDeConjuntos()