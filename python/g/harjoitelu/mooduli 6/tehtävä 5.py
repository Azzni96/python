
def inventaario(lukut ,):

    print("sinulla on seuravat numerot: ")
    for i in lukut :
        print(str(i))

    return lukut

lukut=[(1,2,3,4,5,6,7,8,9,10)]
luku =(2,4,6,8,10)
inventaario(lukut)
list.clear(lukut)
lukut.append(luku)
inventaario(lukut)
