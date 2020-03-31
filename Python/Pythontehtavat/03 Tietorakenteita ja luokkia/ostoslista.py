import sys

lista = [""]
while True:
    i = input("Lisää listalle: ")
    if i != "":
        lista.append(i)
    else:
        break
    print("Listalla on ", len(lista)-1)
    lista.sort()
    for x in lista:
        print(x)
    print("\n")