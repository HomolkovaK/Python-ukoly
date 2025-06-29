import requests

nazev = input("Zadej název subjektu nebo část názvu: ")
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

data = {"obchodniJmeno": nazev}
response = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat",headers=headers,json=data)
subjekt = response.json()

print("Nalezeno subjektů:", subjekt["pocetCelkem"])
for item in subjekt["ekonomickeSubjekty"]:
    print(item["obchodniJmeno"] + ", " + item["ico"])