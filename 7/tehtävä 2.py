nimet = set()
nimi = str(input("anna nimi: "))
print(f"{nimi} on uusi nimi")
nimet.add(nimi)
while nimi != "":
    nimi = str(input("anna nimi: "))
    if nimi in nimet:
        print(f"{nimi} on aiemmin syötetty nimi")
    elif nimi not in nimet and nimi !="":
        print(f"{nimi} on uusi nimi")
        nimet.add(nimi)

print("nimet lista: ")
for n in (nimet):
    print(n)