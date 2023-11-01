kaupunget = []
kaupunki = input("Anna kaupunki: ")

for _ in range(0,5):
    kaupunget.append(kaupunki)
    kaupunki = input("Anna kaupunki: ")

for kaupunki in kaupunget:
    print(kaupunki)


