kuhun_pituus = float(input("Anna kuhun pituus cm: "))
if kuhun_pituus<=37:
    kuhun_uusi_pituus= 37-kuhun_pituus
    print("ei onnistuu: "+str(kuhun_uusi_pituus)+ "cm alimmasta sallitusta pyyntimitasta puuttuu. ")