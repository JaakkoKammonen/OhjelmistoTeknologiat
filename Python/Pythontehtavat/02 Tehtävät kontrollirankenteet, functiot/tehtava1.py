
typed = 0
sum = 0
while True:
    inpu = input("Anna luku, tyhjä lopettaa: ")
    if inpu != "":
        sum = sum + float(inpu)
        typed = typed + 1
    else:
        ka = sum / typed
        print("Lukuja " + str(typed) + " kappaletta")
        print("Summa: " + str(sum))
        print("Keskiarvo: " + str(ka))
        break