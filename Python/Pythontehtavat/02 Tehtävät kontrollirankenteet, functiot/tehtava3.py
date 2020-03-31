
def tulostaTahtia(useri):
    for i in range(0, useri):
        print("*",end="")
    print("")
    

def tulostaNelio(useri):
   for i in range(0,useri):
        for i in range(0, useri):
            print("*",end="")
        print("")
    
    
    
def tulostaSuorakulmio(useri, userii):
    for i in range(0,userii):
        for i in range(0, useri):
            print("*",end="")
        print("")
    print("")


def tulostaKolmio(useri):
     for i in range(0, useri):
        for j in range(0, i+1):
            print("*",end="")
        print("")

def main():
    useri = int(input("Monta tähtee? " ))
    userii = int(input("Monta monta rivii?? "))
    print('Tähdet:')
    tulostaTahtia(useri)
    print('Neliö:')
    tulostaNelio(useri)
    print('Suorakulmio:') 
    tulostaSuorakulmio(useri, userii)
    print('Kolmio:')
    tulostaKolmio(useri)
    #print('Lukusarjan summa n=100:', lukusarjanSumma(100))
    #print('Kertoma n=20', kertoma(20)) 

main()        