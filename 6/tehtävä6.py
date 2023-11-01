import math
def pitsa(halkaisia,hinta):
    säde= (halkaisia/2) / 100
    pintala = math.pi * (säde ** 2)
    arvo = hinta / pintala
    return arvo
halkaisia_1 = int(input("anna halkaisia: "))
hinta_1 = int(input("anna hinta1:"))
halkaisia_2 = int(input("anna halkaisia2: "))
hinta_2 = int(input("anna hinta2: "))

pitsa1 = pitsa(halkaisia_1,hinta_1)
pitsa2 = pitsa(halkaisia_2, hinta_2)


if pitsa1 > pitsa2:
    print("ensinmäinen")
else:
    print("toinen")
