import random
peli = random.randint (1,10)
arvokas = float(input("Anna arvokasmäärä:"))

while peli != arvokas:
    arvokas = float(input("Anna arvokasmäärä:"))
    if arvokas>peli:
     print("Liian suurin.")
    elif arvokas<peli:
     print("Liian pienin.")
print("oli oikein")