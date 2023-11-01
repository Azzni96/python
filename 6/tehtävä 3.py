gallo = float(input("gallonmäärä: "))
litra = 3.785

def gallonmäärä_litroksi():
    gallonmäärä = gallo * litra
    return gallonmäärä


while gallo > 0:

 gallonmäärä = gallonmäärä_litroksi()
 print(gallonmäärä)
 gallo = float(input("gallonmäärä: "))

print()

