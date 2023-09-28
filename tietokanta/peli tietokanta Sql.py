import mysql.connector
def haekentantiedot(Maa):
    sql = f"select country.name, (co2_budget - 9990) as hinta from country, game, airport where airport.iso_country = country.iso_country and country.name = '{Maa}' limit 1;"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(rivi)
    return
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Nihad1996#',
         autocommit=True
         )


Maa = input("Anna haluamasi kentätn MAA: ")
haekentantiedot(Maa)