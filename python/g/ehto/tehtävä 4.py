import random
peli = random.randint (1,10)
arvokas = float(input("Anna arvokasmäärä:"))

while peli != arvokas:
    if peli <arvokas:
        print("Liian suurin.")
    elif peli>arvokas:
          print("Liian pienin.")
    arvokas = float(input("Anna arvokasmäärä:"))

print("oli oikein")