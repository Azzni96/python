class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nykyinen_nopeus,  kuljettumatka):
        self.tunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
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


auto = Auto("ABC-123", 142, 0, 0)
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(auto.nykyinen_nopeus)
auto.hätäjarrutus(-200)
print(auto.nykyinen_nopeus)



