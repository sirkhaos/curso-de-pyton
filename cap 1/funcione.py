def pedir_pizza():
    print("pedir pizza")


pedir_pizza()


def check_entrada(edad):
    if edad < 18:
        print("No puedes entrar")
    elif edad >= 21:
        print("Puedes beber")
    else:
        print("Puedes entrar pero no puedes beber")


edad = 18
check_entrada(edad)
