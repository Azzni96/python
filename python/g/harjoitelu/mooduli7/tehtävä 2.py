nimet = set()
nimi = str(input("anna nimi: "))
nimet.add(nimi)
while nimi != "":
    nimi = str(input("anna nimi: "))
    if nimi in nimet:
        print("Aiemmin syötetty nimi: ")
    elif nimi not in nimet and nimi !="":
        print("uusi nimi: ")
        nimet.add(nimi)

print("nimet lista: ")
for n in (nimet):
 print(n)