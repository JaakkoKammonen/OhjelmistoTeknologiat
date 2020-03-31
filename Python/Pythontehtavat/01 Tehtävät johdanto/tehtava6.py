import datetime
age = int(input("Anna syntymävuotesi: "))
datee = datetime.date.today()
year = datee.year
age2 = datee.year - age
print("Olet nyt " + str(age2) + " vuotta.")
sata = age + 100
print("Täytät sata vuonna " + str(sata))