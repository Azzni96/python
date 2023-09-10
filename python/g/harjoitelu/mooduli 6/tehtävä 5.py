
def poistetaan_parittomat_luvut(luku):
    return [x for x in luku if x % 2 == 0]
list = [1,2,3,4,5,6,7,8,9,10]
print(list)
print(poistetaan_parittomat_luvut(list))