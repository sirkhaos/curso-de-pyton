# fl1 = True
# while fl1:
#     try:
#         op = int(input(
#             "Menu \n 1.- Suma \n 2.- Resta \n 3.- Multiplicasion \n 4.- Division \n 5.- exit \n Escoge tu opcion: "))
#     except ValueError:
#         print("Ese no es un numero")
#     else:
#         resp = 0
#         try:
#             if op > 0 and op < 5:
#                 n1 = int(input("Primer operando: "))
#                 n2 = int(input("Segundo operando: "))
#         except ValueError:
#             print("Debes ingresar un numero")
#         else:
#             if op == 1:
#                 resp = n1+n2
#             elif op == 2:
#                 resp = n1-n2
#             elif op == 3:
#                 resp = n1/n2
#             elif op == 5:
#                 fl1 = False
#             else:
#                 print("Opcion no valida")
#         if op > 0 and op < 5:
#             print("El resultado es: " + str(resp) + "\n")


def calc(op, n1, n2):
    resp = 0

    if op == 1:
        resp = n1+n2
    elif op == 2:
        resp = n1-n2
    elif op == 3:
        resp = n1*n2
    elif op == 4:
        resp = n1/n2
    elif op == 5:
        return False
    else:
        print("Opcion no valida \n")
    if op > 0 and op < 5:
        print("El resultado es: " + str(resp) + "\n")
        return True


rept = True
while rept:
    try:
        ops = int(input(
            "Menu \n 1.- Suma \n 2.- Resta \n 3.- Multiplicasion \n 4.- Division \n 5.- exit \n Escoge tu opcion: "))
    except ValueError:
        print("Debes ingresar un numero \n")
    else:
        try:
            if ops > 0 and ops < 5:
                in1 = int(input("Primer operando: "))
                if type(in1) != int:
                    in1 = 0
                in2 = int(input("Segundo operando: "))
                if type(in2) != int:
                    in2 = 0
            else:
                mensaje = " \n" if ops == 5 else "Escoge un numero dentro del rango \n"
                print(mensaje)
        except ValueError:
            print("Debes ingresar un numero \n")
        else:
            rept = calc(ops, in1, in2)
print("Adios \n")
