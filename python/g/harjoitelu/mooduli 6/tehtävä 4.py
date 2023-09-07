def kokonaisluku(ekä , toka):
    summa = ekä + toka
    return summa
ekä= float(input("anna luku: "))
toka = float(input("anna luku: "))
tulos = kokonaisluku(ekä,toka)
print(f"Lukujen {ekä:.3f} ja {toka:.3f} neliösumma on {tulos:.3f}.")
