karkausvuosi = int(input("Anna vuosiluku: "))
if float(karkausvuosi/4) == int(karkausvuosi/4):
    print("vuosiluku on karkausvuosi")
elif float(karkausvuosi/100) == int(karkausvuosi/100) and float(karkausvuosi/400) == int(karkausvuosi/400):
    print("vuosiluku on karkausvuosi")
else:
    print("vuosiluku ei ole karkausvuosi")