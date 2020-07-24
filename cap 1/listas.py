mylitta = [1, 2, 3, 4, 5]
l2 = list([1, 2, 3, 4, 5])
l3 = list("casa de papel")
l4 = "alberto torres".split()
l5 = "alberto torres,carolina torres,mauricio torres".split(",")
cadena = " - ".join(l5)

mylitta = mylitta + [12, 13]

mylitta += [15, 16]

mylitta.append(9)

mylitta.extend([10, 11])



print(mylitta)

print(l2)
print(l3)
print(l4)
print(l5)
print(cadena)

print(l3.index("s"))

print(l3[-2])
