import random
luku = int(input("heitto napaa: "))
silmäluku= 0
def parametriton_funktio():

    silmäluku = random.randint(1,luku)

    return silmäluku
while silmäluku!= luku:
    parametriton_funktio()
    silmäluku = parametriton_funktio()
    print(silmäluku)
