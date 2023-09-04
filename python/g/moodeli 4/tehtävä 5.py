tuunus = ""
salasana = ""
käyttäjä = 0

while käyttäjä < 5:
    tuunus = str(input("anna tuunus: "))
    salasana = str(input("anna salasana: "))
    käyttäjä +=1
    if tuunus == 'python' and salasana == 'rules':

       print("tervetuloa")
       break

if käyttäjä == 5:
   print("pääsy evätty")
