import random
silmäluku = 0
def parametriton_funktio():
    silmäluku = random.randint(1,6)
    return silmäluku
while silmäluku!= 6:
    parametriton_funktio()
    silmäluku = parametriton_funktio()
    print(silmäluku)
