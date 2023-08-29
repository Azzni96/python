luku = int(input('Anna luku:'))
pienin = suurin = luku
lopeta_toistot = False
while not lopeta_toistot:
    syote = input('Anna luku tai return = lopetus: ')
    if syote != '':
        uusi_luku = int(syote)
        if uusi_luku > suurin:
            suurin = uusi_luku
        elif uusi_luku < pienin:
            pienin = uusi_luku
    else:
        lopeta_toistot = True
print(f'suurin oli {suurin} ja pienin {pienin}.')