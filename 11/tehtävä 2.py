class Auto:
    def __init__(self, rekisterinimi, huipponopeus):
        self.nimi = rekisterinimi
        self.nopeus = huipponopeus

    def tulosta_tiedot(self):
        print(f"{self.nimi}, {self.nopeus} km/h")

class sähköauto(Auto):
    def __init__(self,rekisterinimi, huipponopeus, akkukapasiteetti):
        self.akku = akkukapasiteetti
        super().__init__(rekisterinimi, huipponopeus)
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"{self.akku} kWh")
class polttomoottoriauto(Auto):
    def __init__(self,rekisterinimi, huipponopeus, bensatankin):
        self.bensatankin = bensatankin
        super().__init__(rekisterinimi, huipponopeus)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"{self.bensatankin} l")

Autot=[]
Autot.append(sähköauto("ABC-15", 180, 52.5))
Autot.append(polttomoottoriauto("ACD-123", 165, 32.3))
for A in Autot:
    A.tulosta_tiedot()
#Aseta kummallekin autolle haluamasi nopeus,
# käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.