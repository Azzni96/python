import random

class Auto:
    def __init__(self, rekisteritunnus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = random.randint(100, 200)
        self.kuljettu_matka = 0
        self.nopeus = 0

    def kiihdyta(self):
        muutos = random.randint(-10, 15)
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self):
        self.kuljettu_matka += self.nopeus

def luo_auto_lista():
    auto_lista = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        auto = Auto(rekisteritunnus)
        auto_lista.append(auto)
    return auto_lista

def kilpailu():
    auto_lista = luo_auto_lista()
    tunti = 0

    while True:
        tunti += 1
        for auto in auto_lista:
            auto.kiihdyta()
            auto.kulje()

        for auto in auto_lista:
            if auto.kuljettu_matka >= 10000:
                return auto_lista, tunti

if __name__ == "__main__":
    voittaja_lista, kesto = kilpailu()
    print("Kilpailu päättyi!")
    print("Auto\tRekisteritunnus\tHuippunopeus\tKuljettu Matka")
    for auto in voittaja_lista:
        print(f"{auto.rekisteritunnus}\t{auto.huippunopeus} km/h\t{auto.kuljettu_matka} km")
    print(f"Kilpailu kesti {kesto} tuntia.")
