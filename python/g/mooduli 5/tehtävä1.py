import random

numerot = []
arpakuutioiden_lukumäärän = int(input("anna arpakuutioiden lukumäärän : "))
for _ in range(arpakuutioiden_lukumäärän):
    silmäluku = random.randint(1,6)
    numerot.append(silmäluku)
print(f"silmäluku on: {sum (numerot)}")