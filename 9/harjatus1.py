class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinennopeus, kuljettumatka):
        self.tunnus = rekisteritunnus
        self.nopeus = huippunopeus
        self.nykyinen_nopeus = tämänhetkinennopeus
        self.kulje_matka = kuljettumatka

auto = Auto("ABC-123", 142, 0, 0 )
print(f"Auto on {auto.tunnus}, huippunopeus on {auto.nopeus}Km/h, hetinennopeus on {auto.nykyinen_nopeus} kulje matka {auto.kulje_matka}")



