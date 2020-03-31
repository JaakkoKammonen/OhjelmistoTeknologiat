import datetime
sekuntit = int(input("Anna aika sekunteina: "))
aika= sekuntit
paiva= aika//86400
tunti= (aika-(paiva*86400))//3600
minuutti= (aika - ((paiva*86400) + (tunti*3600)))//60
sekuntti= aika - ((paiva*86400) + (tunti*3600) + (minuutti*60))
print( paiva, 'päivää' , tunti,'tuntia', minuutti, 'minuuttia',sekuntti,' sekunttia')