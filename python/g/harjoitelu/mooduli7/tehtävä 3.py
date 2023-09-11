lentoasemat = {"helsinki-vantaa": "EFHK",
               "helsinki-malmi": "EFHF",
               "jyväskylä": "EFJY",
               "kajaani": "EFKI",
               "forssa": "EFFO"}
lentoasema = ""

while True:
    lentoasema = input("anna lentoasema: ")
    if lentoasema in lentoasemat:
        print(f"lentoasema {lentoasema} ICAO-koodi on {lentoasemat[lentoasema]}.")
    elif lentoasema == "lopettaa":
        break



