import requests

ico = input("Zadej IČO subjektu: ")

response = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")
data = response.json()

print(data["obchodniJmeno"])
print(data["sidlo"]["textovaAdresa"])