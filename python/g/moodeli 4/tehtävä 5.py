username = ""
password = ""
count = 0

while count < 5:
    username = input("Syötä käyttäjätunnus: ")
    password = input("Syötä salasana: ")
    if username == "python" and password == "rules":
        print("Tervetuloa!")
        break
    else:
        print("kirjoita uudelleen.")
        count += 1

if count == 5:
    print("pääsy evätty")
