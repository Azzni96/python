class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nykyinen_nopeus,  kuljettumatka):
        self.tunnus = rekisteritunnus
        self.nopeus = huippunopeus
        self.nykyinen_nopeus = nykyinen_nopeus
        self.kulje_matka = kuljettumatka

    def kiihdyta(self, nopeus_muutos):
        if  nopeus_muutos + self.nykyinen_nopeus < 0 :
            self.nykyinen_nopeus = 0

        elif nopeus_muutos + self.nykyinen_nopeus > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus
        else:
            self.nykyinen_nopeus += self.nykyinen_nopeus + nopeus_muutos

    def hätäjarrutus(self, nopeus_muutos):
        if nopeus_muutos + self.nykyinen_nopeus > 0:
            self.nykyinen_nopeus = 0
        self.nykyinen_nopeus = self.nykyinen_nopeus + nopeus_muutos

    def kulje(self, tuntimäärä):
        self.tuntimäärä = tuntimäärä
        self.kulje_matka += self.nykyinen_nopeus * self.tuntimäärä


auto = Auto("ABC-123", 142, 60, 2000)

auto.kulje(1.5)
print(auto.kulje_matka)



