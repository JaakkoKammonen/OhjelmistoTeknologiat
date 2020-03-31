import random
lista=["Kivi","Paperi","Sakset"]
pelivalinta = random.choice(lista)

while True:
    
    valinta = input("Kivi (1), paperi (2) vai sakset (3)? Tyhjä vastaus lopettaa: ")
    
    if valinta == "1":
        print("Kivi - " + pelivalinta)
        if pelivalinta == "Kivi":
            print("Tasapeli")
            pelivalinta = random.choice(lista)   
        elif pelivalinta == "Sakset":
            print("Kivi voittaa sakset, voitit :)")
            pelivalinta = random.choice(lista)
        else:
            print("Paperi voittaa kiven, hävisit")
            pelivalinta = random.choice(lista)

    if valinta == "2":
        print("Paperi - " + pelivalinta)
        if pelivalinta == "Paperi":
            print("Tasapeli")
            pelivalinta = random.choice(lista)   
        elif pelivalinta == "Sakset":
            print("Sakset voittaa paperin, hävisit")
            pelivalinta = random.choice(lista)
        else:
            print("Paperi voittaa kiven, voitit :)")
            pelivalinta = random.choice(lista)

    if valinta == "3":
        print("Sakset - " + pelivalinta)
        if pelivalinta == "Sakset":
            print("Tasapeli")
            pelivalinta = random.choice(lista)   
        elif pelivalinta == "Paperi":
            print("Sakset voittaa paperin, voitit")
            pelivalinta = random.choice(lista)
        else:
            print("Kivi voittaa sakset, hävisit")
            pelivalinta = random.choice(lista)
            
    if valinta == "":
        break