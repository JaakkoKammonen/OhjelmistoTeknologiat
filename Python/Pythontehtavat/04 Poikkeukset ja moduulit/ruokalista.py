import requests

r = requests.get("https://www.fazerfoodco.fi/modules/json/json/Index?costNumber=0083&language=fi")
json = r.json()
name = json['RestaurantName']
text = json['Footer']
korona = "Koronan takia ei ole ruokaa... sniff"

print(name)
print("")
print(korona)
print("")
print(text)