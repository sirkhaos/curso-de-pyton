edad = 18

if edad < 18:
    print("No puedes entrar")
elif edad >= 21:
    print("Puedes beber")
else:
    print("Puedes entrar pero no puedes beber")

nombre = "alberto"
apellido = "torres"


def pedir_alcohol():
    if(edad < 21):
        print("no puedes beber")
    else:
        print("tu pedido estara en breve " + nombre + "\n")


pedir_alcohol()
