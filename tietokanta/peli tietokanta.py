

def ruotsi(coins):
    print("Tervetuloa matkalle Ruotsiin!")

#Kysymys1
    while True:
        vastaus = input("Ruotsi on euroopan pohjoisin valtio. (oikein/väärin): ").lower()
        if vastaus == "väärin":
            print("Onnea, oikea vastaus! Ansaitsit 5 kolikon :)")
            coins += 5
            break
        elif vastaus == "oikein":
            print("Väärä vastaus, hävisit 2 kolikkoa :(")
            coins -= 2
            break
        else:
            print("Syötä vastaus uudelleen")

#Kysymys2
    while True:
        vastaus = input(f"Ruotsi kuuluu skandinaviaan. (oikein/väärin): ").lower()
        if vastaus == "oikein":
            print("Oikea vastaus! Ansaitsit 5 kolikon!")
            coins += 5
            break
        elif vastaus == "väärin":
            print("Väärä vastaus, hävisit 2 kolikkoa :(")
            coins -= 2
            break
        else:
            print("Syötä vastaus uudelleen")

#Kysymys3
    while True:
        R3 = input("""Ruotsin eteläisin kaupunki on \nA: Malmö \nB: Skellefteå \nC: Tukholma\nD: Umeå\nVastaus: """).upper()
        if R3 == "A":
            print("Oikea vastaus, Ansaitsit 5 kolikon! :)")
            coins += 5
            break
        elif R3 in ("B", "C", "D"):
            print("Väärä vastaus, hävisit 2 kolikkoa :(")
            coins -= 2
            break
        elif R3 not in ("A", "B", "C", "D"):
            print("Virheellinen vastaus, valitse vaihtoehdoista A,B,C tai D")
    print(f"Sinulla on {coins} kolikkoa")
    return coins



def norja(coins):
#kyssäri1
    while True:
        N1 = input("Norjan lipussa on punaista ja keltaista (oikein/väärin):").lower()
        if N1 == "oikein":
            print("Väärä vastaus, hävisit 2 kolikkoa :(")
            coins -= 2
            break
        elif N1 == "väärin":
            print("Onnea, oikea vastaus! Ansaitsit 5 kolikon :)")
            coins += 5
            break
        else:
            print("Syötä vastaus uudelleen")


#kyssäri2
    while True:
        N2 = str(input("Norjassa puhutaan saamen kieltä (oikein/väärin): ")).lower()
        if N2 == "oikein":
           print("Oikea vastaus! Ansaitsit 5 kolikon!")
           coins+=5
           break
        elif N2 == "väärin":
            print("Väärä vastaus, hävisit 2 kolikkoa :(")
            coins -= 2
            break
        elif N2 != "oikein" or "o" or "väärin" or "v":
                    print("Virheellinen vastaus, syötä oikein tai väärin:")


#kyssäri3
    while True:
        N3 = input("""Norjan länsipuolella sijaitsee \nA: Atlantin valtameri \nB: Itämeri \nC: Punainen meri\nD: Saimaa\nVastaus: """).upper()
        if N3 == "A":
            print("Oikea vastaus, Ansaitsit 5 kolikon! :)")
            coins+=5
            break
        elif N3 in ["B", "C", "D"]:
            print("Väärä vastaus, hävisit 2 kolikkoa :(")
            coins -= 2
            break
        elif N3 not in ("A", "B", "C", "D"):
            print("Virheellinen vastaus, valitse vaihtoehdoista A,B,C tai D")
    print(f"Sinulla on {coins} kolikkoa")
    return coins



def Isobritannia(coins):
    # kyssäri1
    while True:
        I1 = input("Onko Cillian Myrphy englantilainen? (oikein/väärin) :").lower()
        if I1 == "oikein":
            print("Väärä vastaus, hävisit 2 kolikkoa :(")
            coins -= 2
            break
        elif I1 == "väärin":
            print("Onnea, oikea vastaus! Ansaitsit 5 kolikon :)")
            coins += 5
            break
        else:
            print("Syötä vastaus uudelleen")

    # kyssäri2
    while True:
        I2 = str(input("Keitetyt pavut kuuluvat englantilaiseen aamupalaan? (oikein/väärin): ")).lower()
        if I2 == "oikein":
            print("Oikea vastaus! Ansaitsit 5 kolikon!")
            coins += 5
            break
        elif I2 == "väärin":
            print("Väärä vastaus, hävisit 2 kolikkoa :(")
            coins -= 2
            break
        elif I2 != "oikein" or "o" or "väärin" or "v":
            print("Virheellinen vastaus, syötä oikein tai väärin:")

    # kyssäri3
    while True:
        I3 = input(
            """Kuka englantilainen julkisuuden henkilö kuoli hiljattain \nA: Queen Elizabeth \nB: Boris Johnson \nC: Harry Styles\nD: Lily McHardin\nVastaus: """).upper()
        if I3 == "A":
            print("Oikea vastaus, Ansaitsit 5 kolikon! :)")
            coins += 5
            break
        elif I3 in ("B" or "C" or "D"):
            print("Väärä vastaus, hävisit 2 kolikkoa :(")
            coins -= 2
            break
        elif I3 not in ("A" or "B" or "C" or "D"):
            print("Virheellinen vastaus, valitse vaihtoehdoista A,B,C tai D")
    print(f"Sinulla on {coins} kolikkoa")





Vieraillut_maat = []
maxcoins_voittaa = 120
coins = 0
print("Hei! Valitse alla olevasta listasta mihin kohteeseen haluat matkustaa?")

print("Ruotsi")
print("Norja")
print("Iso-Britannia")
print("Saksa")
print("Belgia")
print("Espanja")
print("Kreikka")
print("Italia")
print("Puola")
print("Portugal")


#ABC
while True:
    valtio = str(input("Minne haluat matkustaa?: ")).lower()
    if valtio in  ("ruotsi","norja","iso-britannia", "saksa", "belgia" , "espanja" , "portugal", "kreikka", "italia", "puola"):
        if valtio in Vieraillut_maat:
            print(f"Olet jo matkustanut kohteeseen {valtio}. Valitse toinen kohde.")
        else:
            Vieraillut_maat.append(valtio)
            print(f"Matkustetaan kohteeseen {valtio}!")
            if valtio == "ruotsi":
                 coins= ruotsi(coins)
            elif valtio == "norja":
                 coins= norja(coins)
            elif valtio == "iso-britannia":
                 coins = Isobritannia(coins)
            elif maxcoins_voittaa >= coins:
                 print("Voitit")
                 break
    elif valtio == "exit":
        print("Kiitos pelaamisesta!")
        print(f"Sinulla on yhteensä {coins} kolikkoa.")
        break

    else:
         print("Valitse jokin kohteista tai kirjoita 'exit' lopettaaksesi pelin.")

