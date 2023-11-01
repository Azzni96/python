luku = int(input("Anna luku: "))
suuri = pieni =luku
lopetus_maara = False
while not lopetus_maara:
    luku = input('Uudelleen anna luku tai return = lopettaa: ')
    if luku != "":
        uusi_luku = int(luku)
        if uusi_luku > suuri:
            suuri = uusi_luku
        elif uusi_luku < pieni:
            pieni = uusi_luku
    else:
        lopetus_maara = True
print (f'{suuri} + oli suurin + {pieni} oli pienin.')

