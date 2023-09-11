vuodenajat = ("talvi", "talvi", "kevät", "kevät","kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
järjestysnumero = int(input("Anna vuodenaika järjestysnumero (1-12): "))
vuodenaika = vuodenajat[järjestysnumero-1]
print (f"{järjestysnumero}. viikonpäivä on {vuodenaika}.")