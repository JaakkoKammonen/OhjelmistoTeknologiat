valinta = input("Isoiksi(1) vai pieniksi(2)? Muu syöttö ei tee mitään. ")

if valinta == "1":
    with open ("loremipsum.txt") as file_in:
        lines = file_in.read().upper()
    with open ("loremipsum.txt","w") as file_out:    
        file_out.write(lines)
    print("Tiedoston kirjaimet vaihdettu isoiksi")
elif valinta == "2":
    with open ("loremipsum.txt") as file_in:
        lines = file_in.read().lower()
    with open ("loremipsum.txt","w") as file_out:    
        file_out.write(lines)
    print("Tiedoston kirjaimet vaihdettu pieneksi")
else:
    print("Toimenpiteitä ei tehty")
    