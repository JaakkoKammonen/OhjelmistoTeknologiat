from datetime import date 

syote = input("Anna syntymäpäivä muodossa d.m.yyy: ")
if len(syote) > 10 or len(syote) < 10:
    print("Väärä syöte!")

paiva = int(syote[0:2])
kk = int(syote[3:5])
v = int(syote[6:10])
try:
    synttari = date(v,kk,paiva)
except:
    print("Syötit väärin synttäris! ei onnaa siis")

def laskeika():
    tanaan = date.today()
    ikapaiva = synttari - tanaan
    ikapaiva = str(ikapaiva.days)
    ikapaivao = ikapaiva[1:]
    ikav = date.today().year - v
    print("Olet nyt", ikav,", tarkemmin sanoen", ikapaivao,"päivää")
  
    
laskeika()