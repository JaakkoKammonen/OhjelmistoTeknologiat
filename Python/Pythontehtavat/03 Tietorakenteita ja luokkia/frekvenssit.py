
allletters = "abcdefghijklmnopqrxyzåäö"
letters = [i for i in allletters]
amount = 0

with open('luku1.txt', encoding='utf-8') as file_in:
    file = file_in.read().lower()
fileletters = {}
for i in letters:
    fileletters[i] = file.count(i)
    amount = amount + fileletters[i]

print("Kirjaimia yhteensä: ",amount)

for i in fileletters:
    print(i, ":", round(100* fileletters[i]/amount,2), "%")
