vocales = "aeiou"
lista_vocales = list(vocales)

"a" in vocales
# true
"z" in vocales
# false
"a" in lista_vocales
# true
"z" in lista_vocales
# false

if "a" in vocales:
    print("a es una vocal")
if "z" not in vocales:
    print("z no es una vocal")
