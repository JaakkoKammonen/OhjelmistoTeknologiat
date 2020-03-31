paino = float(input("Syötä painosi: "))
pituus = float(input("Syötä pituutesi senttimetreinä: "))
teksti = "Paino on x"
mpituus = pituus / 100
bmi = paino / mpituus / mpituus
if bmi < 18.5:
    teksti = "Painoindeksi: " + str("{:.2f}".format(bmi)) + ". Paino on ihannetta pienempi"
    print (teksti)
elif bmi >= 18.5 and not bmi > 24.9:
    teksti = "Painoindeksi: " + str("{:.2f}".format(bmi)) + ". Se on ihanne."
    print (teksti)
elif bmi >= 25.0 and not bmi >= 29.9:
    teksti = "Painoindeksi: " + str("{:.2f}".format(bmi)) + ". Sinulla on lievää ylipainoa"
    print (teksti)
elif bmi >= 30 and not bmi >= 34.9:
    teksti = "Painoindeksi: " + str("{:.2f}".format(bmi)) + ". Sinulla on merkittävää ylipainoa"
    print (teksti)
elif bmi >= 35 and not bmi >= 39.9:
    teksti = "Painoindeksi: " + str("{:.2f}".format(bmi)) + ". Sinulla on vaikea lihavuus"
    print (teksti)
elif bmi > 40:
    teksti = "Painoindeksi: " + str("{:.2f}".format(bmi)) + ". Sinä ole sairaalloisen lihava"
    print (teksti)
