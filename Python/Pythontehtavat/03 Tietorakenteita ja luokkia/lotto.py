import random
 


def lottoarvonta():
    numerot = list(range(1,41))
    lottorivi = random.sample(numerot, 7)
    for i in lottorivi:
        numerot.remove(i)
    lisanumerot = random.sample(numerot, 3)  
    return lottorivi,lisanumerot

def pelaa():
    omarivi = lottoarvonta()
    lottorivi = omarivi[0]
    lisanumerot = omarivi[1]
    return lottorivi, lisanumerot

def tarkista(arvonta, rivi):
    oikeat = arvonta
    omarivi = rivi
    normirivitulos = []
    lisarivi=[]
    for i in omarivi[0]:
        if i in oikeat[0]:
            normirivitulos.append(i)
    for i in omarivi[1]:
        if i in oikeat[1]:
            lisarivi.append(i)        
    print(len(normirivitulos) , "oikein", normirivitulos, "ja",len(lisarivi), "lisänumeroa" , lisarivi)
    #print(oikeat, omarivi)


arvonta = lottoarvonta()
print('Oikea rivi:', end = ' ')
print(*arvonta[0], sep = ', ') # näinkin voi tehdä!
print('Lisänumerot:', end = ' ')
print(*arvonta[1], sep = ', ') 
rivi = pelaa() 
print('Rivi:', end=' ')
print(*rivi[0], sep = ', ')
print('Lisänumerot:', end = ' ')
print(*rivi[1], sep = ', ') 
tarkista(arvonta, rivi) 