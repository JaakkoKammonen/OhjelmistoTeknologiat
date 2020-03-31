import sys

# komentorivin sisältö on saatavissa taulukossa sys.argv
# jos haluat nähdä komentoriviparametrit: print(sys.argv)
#
# komennolla $ python muunnos.py --upper inputfile.txt outputfile.txt
# argv:n sisältö olisi ['muunnos.py', '--upper', 'inputfile.txt', 'outputfile.txt']

if len(sys.argv) != 4 or sys.argv[1] not in ['--upper', '--lower']:
    print("Käyttö: python muunnos.py --upper|--lower <mista-tiedosto> <mihin-tiedosto>")
    sys.exit(1)
else:
    muunnos = sys.argv[1]
    mistaTiedosto = sys.argv[2]
    mihinTiedosto = sys.argv[3]
