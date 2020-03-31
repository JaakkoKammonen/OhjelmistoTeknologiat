import math
kat1 = int(input("Anna kateetti 1: "))
kat2 = int(input("Anna kateetti 2: "))
pintaala = (kat1 * kat2)/2
print("Kolmion pintal-ala: " + str(pintaala))
hypo = math.sqrt((kat1 * kat1) + (kat2 * kat2))
print("Hypotenuusa: " + str("{:.2f}".format(hypo)))
