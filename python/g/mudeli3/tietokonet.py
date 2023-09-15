import mysql.connector
import config
def suoritaSQLhaku(sql):

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user="root" ,
         password="Nihad1996#",
         autocommit=True
         )
icao = input("Anna haluamasi kentätn ICAO-koodi: ")
sql = "select name, municipality from airport where ident ='" +icao+"'";
tulos = suoritaSQLhaku(sql)

for rivi in tulos:
    print(rivi)