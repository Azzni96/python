import mysql.connector
tt
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='airport',
         user='root',
         password='12345',
         autocommit=True
         )


pisteet = 0
list = []
def haeKentat():
    sql = "select name from country where questions = 'yes'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            #print(rivi[0])
            list.append(rivi[0])
    return
#ruotsi-funktio
def ruotsi(coins):
    print("Tervetuloa matkalle Ruotsiin!")

    # Kysymys 2 - Oikein/Väärin
    while True:
        vastaus = input("Ruotsi on euroopan pohjoisin valtio. (oikein/väärin): ").lower()
        if vastaus == "väärin":
            print("Onnea, oikea vastaus! Ansaitsit 5 kolikon :)")
            coins += 5 #saa 5 coins jos vastaus on oikein
            break
        elif vastaus == "oikein":
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Syötä vastaus uudelleen")

    # Kysymys 2 - Oikein/Väärin
    while True:
        vastaus = input(f"Ruotsi kuuluu skandinaviaan. (oikein/väärin): ").lower()
        if vastaus == "oikein":
            print("Oikea vastaus! Ansaitsit 5 kolikon!")
            coins += 5
            break
        elif vastaus == "väärin":
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Syötä vastaus uudelleen")

    # Monivalintakysymys
    while True:
        R3 = input("""Ruotsin eteläisin kaupunki on \nA: Malmö \nB: Skellefteå \nC: Tukholma\nD: Umeå\nVastaus: """).upper()
        if R3 == "A":
            print("Oikea vastaus, Ansaitsit 5 kolikon! :)")
            coins += 5
            break
        elif R3 in ("B", "C", "D"):
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        elif R3 not in ("A", "B", "C", "D"):
            print("Virheellinen vastaus, valitse vaihtoehdoista A,B,C tai D")
    if coins >= 15:   # jos kaikki kysymykset on oikein
       coins +=5
    print(f"Sinulla on {coins} kolikkoa")
    return coins


#norja-funktio
def norja(coins):
    print("Tervetuloa matkalle Norjaan!")
    # Kysymys 1 - Oikein/Väärin
    while True:
        N1 = input("Norjan lipussa on punaista ja keltaista (oikein/väärin):").lower()
        if N1 == "oikein":
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        elif N1 == "väärin":
            print("Onnea, oikea vastaus! Ansaitsit 5 kolikon :)")
            coins += 5
            break
        else:
            print("Syötä vastaus uudelleen")


    # Kysymys 2 - Oikein/Väärin
    while True:
        N2 = str(input("Norjassa puhutaan saamen kieltä (oikein/väärin): ")).lower()
        if N2 == "oikein":
           print("Oikea vastaus! Ansaitsit 5 kolikon!")
           coins+=5
           break
        elif N2 == "väärin":
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        elif N2 != "oikein" or "o" or "väärin" or "v":
                    print("Virheellinen vastaus, syötä oikein tai väärin:")

    # Monivalintakysymys
    while True:
        N3 = input("""Norjan länsipuolella sijaitsee \nA: Atlantin valtameri \nB: Itämeri \nC: Punainen meri\nD: Saimaa\nVastaus: """).upper()
        if N3 == "A":
            print("Oikea vastaus, Ansaitsit 5 kolikon! :)")
            coins+=5
            break
        elif N3 in ["B", "C", "D"]:
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        elif N3 not in ("A", "B", "C", "D"):
            print("Virheellinen vastaus, valitse vaihtoehdoista A,B,C tai D")
    if coins >= 15:
       coins +=5
    print(f"Sinulla on {coins} kolikkoa")
    return coins


# isobritannia-funktio
def Isobritannia(coins):
    print("Tervetuloa matkalle Iso-britanniaan!")
    # Kysymys 1 - Oikein/Väärin
    while True:
        I1 = input("Onko Cillian Myrphy englantilainen? (oikein/väärin) :").lower()
        if I1 == "oikein":
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        elif I1 == "väärin":
            print("Onnea, oikea vastaus! Ansaitsit 5 kolikon :)")
            coins += 5
            break
        else:
            print("Syötä vastaus uudelleen")

    # Kysymys 2 - Oikein/Väärin
    while True:
        I2 = str(input("Keitetyt pavut kuuluvat englantilaiseen aamupalaan? (oikein/väärin): ")).lower()
        if I2 == "oikein":
            print("Oikea vastaus! Ansaitsit 5 kolikon!")
            coins += 5
            break
        elif I2 == "väärin":
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        elif I2 != "oikein" or "o" or "väärin" or "v":
            print("Virheellinen vastaus, syötä oikein tai väärin:")

    # Monivalintakysymys
    while True:
        I3 = input(
            """Kuka englantilainen julkisuuden henkilö kuoli hiljattain \nA: Queen Elizabeth \nB: Boris Johnson \nC: Harry Styles\nD: Lily McHardin\nVastaus: """).upper()
        if I3 == "A":
            print("Oikea vastaus, Ansaitsit 5 kolikon! :)")
            coins += 5
            break
        elif I3 in ("B" or "C" or "D"):
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        elif I3 not in ("A" or "B" or "C" or "D"):
            print("Virheellinen vastaus, valitse vaihtoehdoista A,B,C tai D")
    if coins >= 15:
       coins +=5
    print(f"Sinulla on {coins} kolikkoa")
    return coins
# saksa-funktio
def saksa(coins):
    print("Tervetuloa matkalle Saksaan!")

    # Kysymys 1 - Oikein/Väärin
    while True:
        vastaus1 = input("Onko Saksan pääkaupunki Berliini? (oikein/väärin): ").lower()
        if vastaus1 == "oikein":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus1 == "väärin":
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Syötä vastaus uudelleen (oikein/väärin)")

    # Kysymys 2 - Oikein/Väärin
    while True:
        vastaus2 = input("Saksassa juodaan paljon teetä. (oikein/väärin): ").lower()
        if vastaus2 == "väärin":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus2 == "oikein":
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Syötä vastaus uudelleen (oikein/väärin)")

    # Monivalintakysymys
    while True:
        vastaus3 = input("Mikä on Saksan virallinen kieli? \nA: Saksa \nB: Ranska \nC: Espanja \nD: Italia \nVastaus: ").upper()
        if vastaus3 == "A":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus3 in ("B", "C", "D"):
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Valitse vaihtoehdoista A, B, C tai D")
    if coins >= 15:
       coins +=5
    print(f"Sinulla on {coins} kolikkoa")
    return coins
# belgia-funktio
def belgia(coins):
    print("Tervetuloa matkalle Belgiaan!")

    # Kysymys 1 - Oikein/Väärin
    while True:
        vastaus1 = input("Onko Belgian pääkaupunki Bryssel? (oikein/väärin): ").lower()
        if vastaus1 == "oikein":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus1 == "väärin":
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Syötä vastaus uudelleen (oikein/väärin)")

    # Kysymys 2 - Oikein/Väärin
    while True:
        vastaus2 = input("Belgiassa syödään paljon suklaata. (oikein/väärin): ").lower()
        if vastaus2 == "oikein":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus2 == "väärin":
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Syötä vastaus uudelleen (oikein/väärin)")

    # Monivalintakysymys
    while True:
        vastaus3 = input("Mikä on Belgian virallinen kieli? \nA: Ranska \nB: Hollanti \nC: Saksa \nD: Englanti \nVastaus: ").upper()
        if vastaus3 == "B":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus3 in ("A", "C", "D"):
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Valitse vaihtoehdoista A, B, C tai D")
    if coins >= 15:
       coins +=5
    print(f"Sinulla on {coins} kolikkoa")
    return coins
# espanja-funktio
def espanja(coins):
    print("Tervetuloa matkalle Espanjaan!")

    # Kysymys 1 - Oikein/Väärin
    while True:
        vastaus1 = input("Onko Espanjassa virallinen kieli espanja? (oikein/väärin): ").lower()
        if vastaus1 == "oikein":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus1 == "väärin":
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Syötä vastaus uudelleen (oikein/väärin)")

    # Kysymys 2 - Oikein/Väärin
    while True:
        vastaus2 = input("Espanjalaiset juhlivat kuuluisaa karnevaalia. (oikein/väärin): ").lower()
        if vastaus2 == "oikein":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus2 == "väärin":
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Syötä vastaus uudelleen (oikein/väärin)")

    # Monivalintakysymys
    while True:
        vastaus3 = input("Mikä on Espanjan tunnetuin tanssi? \nA: Salsa \nB: Flamenco \nC: Samba \nD: Tango \nVastaus: ").upper()
        if vastaus3 == "B":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus3 in ("A", "C", "D"):
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Valitse vaihtoehdoista A, B, C tai D")
    if coins >= 15:
       coins +=5
    print(f"Sinulla on {coins} kolikkoa")
    return coins
# portugali-funktio
def portugali(coins):
    print("Tervetuloa matkalle Portugaliin!")

    # Kysymys 1 - Oikein/Väärin
    while True:
        vastaus1 = input("Onko Portugalin virallinen kieli portugali? (oikein/väärin): ").lower()
        if vastaus1 == "oikein":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus1 == "väärin":
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Syötä vastaus uudelleen (oikein/väärin)")

    # Kysymys 2 - Oikein/Väärin
    while True:
        vastaus2 = input("Portugalissa juodaan paljon teetä. (oikein/väärin): ").lower()
        if vastaus2 == "väärin":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus2 == "oikein":
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Syötä vastaus uudelleen (oikein/väärin)")

    # Monivalintakysymys
    while True:
        vastaus3 = input("Mikä on Portugalin pääkaupunki? \nA: Madrid \nB: Lissabon \nC: Rooma \nD: Ateena \nVastaus: ").upper()
        if vastaus3 == "B":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus3 in ("A", "C", "D"):
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Valitse vaihtoehdoista A, B, C tai D")
    if coins >= 15:
       coins +=5
    print(f"Sinulla on {coins} kolikkoa")
    return coins
# kreikka-funktio
def kreikka(coins):
    print("Tervetuloa matkalle Kreikkaan!")

    # Kysymys 1 - Oikein/Väärin
    while True:
        vastaus1 = input("Onko Kreikka tunnettu antiikin aikaisesta kulttuuristaan? (oikein/väärin): ").lower()
        if vastaus1 == "oikein":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus1 == "väärin":
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Syötä vastaus uudelleen (oikein/väärin)")

    # Kysymys 2 - Oikein/Väärin
    while True:
        vastaus2 = input("Kreikassa syödään paljon pizzaa. (oikein/väärin): ").lower()
        if vastaus2 == "väärin":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus2 == "oikein":
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Syötä vastaus uudelleen (oikein/väärin)")

    # Monivalintakysymys
    while True:
        vastaus3 = input("Mikä on Kreikan pääkaupunki? \nA: Ateena \nB: Rooma \nC: Lissabon \nD: Madrid \nVastaus: ").upper()
        if vastaus3 == "A":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus3 in ("B", "C", "D"):
            print("Väärä vastaus, menetät 2 kolikkoa :(")

            break
        else:
            print("Valitse vaihtoehdoista A, B, C tai D")
    if coins >= 15:
       coins +=5
    print(f"Sinulla on {coins} kolikkoa")
    return coins

# Italia-funktio
def italia(coins):
    print("Tervetuloa matkalle Italiaan!")

    # Kysymys 1 - Oikein/Väärin
    while True:
        vastaus1 = input("Onko Italia kuuluisa pasta-ruoistaan? (oikein/väärin): ").lower()
        if vastaus1 == "oikein":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus1 == "väärin":
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Syötä vastaus uudelleen (oikein/väärin)")

    # Kysymys 2 - Oikein/Väärin
    while True:
        vastaus2 = input("Italiassa puhutaan paljon ranskaa. (oikein/väärin): ").lower()
        if vastaus2 == "väärin":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus2 == "oikein":
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Syötä vastaus uudelleen (oikein/väärin)")

    # Monivalintakysymys
    while True:
        vastaus3 = input("Mikä on Italian pääkaupunki? \nA: Rooma \nB: Ateena \nC: Pariisi \nD: Madrid \nVastaus: ").upper()
        if vastaus3 == "A":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus3 in ("B", "C", "D"):
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Valitse vaihtoehdoista A, B, C tai D")
    if coins >= 15:
       coins +=5
    print(f"Sinulla on {coins} kolikkoa")
    return coins

# Puola-funktio
def puola(coins):
    print("Tervetuloa matkalle Puolaan!")

    # Kysymys 1 - Oikein/Väärin
    while True:
        vastaus1 = input("Onko Puola Euroopan unionin jäsenvaltio? (oikein/väärin): ").lower()
        if vastaus1 == "oikein":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus1 == "väärin":
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Syötä vastaus uudelleen (oikein/väärin)")

    # Kysymys 2 - Oikein/Väärin
    while True:
        vastaus2 = input("Puolassa puhutaan pääasiassa venäjää. (oikein/väärin): ").lower()
        if vastaus2 == "väärin":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus2 == "oikein":
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Syötä vastaus uudelleen (oikein/väärin)")

    # Monivalintakysymys
    while True:
        vastaus3 = input("Mikä on Puolan pääkaupunki? \nA: Varsova \nB: Berliini \nC: Budapest \nD: Pariisi \nVastaus: ").upper()
        if vastaus3 == "A":
            print("Oikea vastaus! Ansaitset 5 kolikkoa! :)")
            coins += 5
            break
        elif vastaus3 in ("B", "C", "D"):
            print("Väärä vastaus, et saanut kolikkoa :(")
            break
        else:
            print("Valitse vaihtoehdoista A, B, C tai D")
    if coins >= 15:
       coins +=5
    print(f"Sinulla on {coins} kolikkoa")
    return coins




print("Hei! Valitse alla olevasta listasta mihin kohteeseen haluat matkustaa?") #tulostaa mihin valtiot pelaja matkustaa

print("Ruotsi")
print("Norja")
print("Iso-Britannia")
print("Saksa")
print("Belgia")
print("Espanja")
print("Kreikka")
print("Italia")
print("Puola")
print("Portugali")
vieraillut_maat = [] #valtio listä
coins = 25 #paljonko rahoja pelajalle on alussa

matkustamisen_hinta = {
    "ruotsi": 10,
    "norja": 10,
    "iso-britannia": 10,
    "saksa": 10,
    "belgia": 10,
    "espanja": 10,
    "portugali": 10,
    "kreikka": 10,
    "italia": 10,
    "puola": 10,
    "ranska": 100  # Lisää Ranskan hinta
}



#ABC
while True:
    valtio = str(input("Minne haluat matkustaa?: ")).lower()
    if valtio in vieraillut_maat:   #koodi ei onnistuu käydä sama valtio kaksi kertaa
        print(f"Olet jo matkustanut kohteeseen {valtio}. Valitse toinen kohde.")
    elif valtio in matkustamisen_hinta:
        hinta = matkustamisen_hinta[valtio]
        if coins < hinta: #koodi ei onnistuu matkustaa toinen valtioon jos hänelle vähän coins
            print(f"Valitettavasti sinulla ei ole tarpeeksi kolikoita matkustaaksesi {valtio}iin. Matkustaminen maksaa {hinta} kolikkoa.")
        else:
            print(f"Matkustetaan {valtio}iin!")
            coins -= hinta #maksuu matkaa hinta
            vieraillut_maat.append(valtio) #lisätä valtio lsitässä

            if valtio == "ruotsi":
                 coins= ruotsi(coins)
            elif valtio == "norja":
                 coins= norja(coins)
            elif valtio == "iso-britannia":
                 coins = Isobritannia(coins)
            elif valtio == "saksa":
                 coins = saksa(coins)
            elif valtio == "belgia":
                 coins = belgia(coins)
            elif valtio == "espanja":
                 coins == espanja(coins)
            elif valtio == "portugali":
                 coins = portugali(coins)
            elif valtio == "kreikka":
                 coins = kreikka(coins)
            elif valtio == "italia":
                 coins = italia(coins)
            elif valtio == "puola":
                 coins = puola(coins)

    if valtio == "exit": #jos ei haluaa jatkaa pelissa
            print("Kiitos pelaamisesta!")
            print(f"Sinulla on yhteensä {coins} kolikkoa.")
            break

    else: #kertää mitä voit tehdä jatkussa
         print("Valitse jokin kohteista tai kirjoita 'exit' lopettaaksesi pelin.")