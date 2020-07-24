#agregar contacto
#remover contacto
#actualisar contacto
#ver contacto
#ver todos los contactos

agenda = dict()

def imprimir (nombre):
    print() #formato de menbrete
    print(nombre)
    print() #formato de piede texto

def add():
    nombre = input("Nombre del contacto: ")
    numero = input("numero del contacto: ")
    agenda[nombre]= numero

def delt():
    nombre = input("Nombre del contacto: ")
    try:
        del agenda[nombre]
    except KeyError:
        #"el contacto {} no existe".format(nombre)
        print("el contacto "+nombre+" no existe")
def edit():
    nombre = input("Nombre del contacto: ")
    numero = input("numero del contacto: ")
    agenda[nombre]=numero
def show(desf=0):
    if desf == 0:
        #intr = "{' {} ': ' {} ' }".format(mombre, agenda[nombre])
        #intr += "{' {} ': ' {} ' }".format(mombre, agenda[nombre])
        intr=agenda
    else:
        nombre = input("Nombre del contacto: ")
        try:
            intr="{'"+nombre +"': '"+agenda[nombre]+"'}"
        except KeyError:
            intr="el contacto " + nombre + "no existe"
    print(intr)

print("Abriendo agenda")
while True:
    print("____________________________")
    print("agenda de contactos")
    print("----------------------------")
    print("------------Menu------------")
    print("1: Agregar contacto")
    print("2: Eliminar contacto")
    print("3: Editar contacto")
    print("4: Ver contacto")
    print("5: Ver Agenda")
    print("6: Salir")
    print("----------------------------")
    try:
        ops = int(input(": "))
    except ValueError:
        print("solo se pueden escoger numenos del 1 al 6")
    else:
        if ops ==1:
            add()
        elif ops==2:
            delt()
        elif ops==3:
            edit()
        elif ops==4:
            show(1)
        elif ops==5:
            show()
        elif ops == 6:
            break
        else:
            print("opsion no valida")