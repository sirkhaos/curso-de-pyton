import random

#sistena de vidas (5)
#sistema de pista(si es mayor o menor)
#volver a jugar
#dificultades:
#               fasil
#               medio rango del 1 al 40
#               dificil 4 intento
#               infierno 3 intento

def rest():
    restart = input("jugar denuevo? si/no \n")
    if restart.lower() == "si":
        play()

def play():
    dificultad = None #vasio
    limite=5
    intentos=0
    while dificultad==None or dificultad>4 or dificultad<1:
        try:
            dificultad = int(input("escoge el nivel de dificultad \n"
                               "1 - facil\n"
                               "2 - medio\n"
                               "3 - dificil\n"
                               "4 - infierno \n"))
        except ValueError:
            print("debes ingresar un numero")
        else:
            if dificultad==1:
                n1 = 1
                n2 = 10
            elif dificultad==2:
                n1 = 1
                n2 = 40
            elif dificultad==3:
                n1 = 1
                n2 = 40
                limite=4
            elif dificultad==4:
                n1 = 1
                n2 = 40
                limite = 3
            else:
                print("opcion no valida")

    elNumero = random.randint(n1,n2)

    print("adivina el numero en {} intentos".format(limite))
    print("esta entre "+ str(n1) +" y " + str(n2))
    def pista(resp):
        if resp<elNumero:
            print("psss, es mayor!!!")
        else:
            print("pss, es menor")

    while intentos<limite:
        try:
            respuesta=int(input("El numero es: "))
        except ValueError:
            print("debes ingresar solo numeros")
        else:
            if respuesta==elNumero:
                print("Has adivinado")
                rest()
                break
            else:
                intentos+=1
                print("noooooo intenta denuevo")
                print("te quedan {} intentos".format(limite-intentos))
                pista(respuesta)

    else:
        print("ooo se te acabaron los intentos juega denuevo :D")
        rest()

play()