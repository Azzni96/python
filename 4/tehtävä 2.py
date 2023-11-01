luku = []
syote = input("luku määrä: ")
while syote!="":
    luku.append(int(syote))
    luku.sort(reverse=True)
    syote = input("luku määrä: ")
print(luku[:5])
