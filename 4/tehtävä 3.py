num = int(input("anna numerot: "))
if num > 2:
    for i in range(2,num):
        if (num % i) == 0:
            print("se ei ole alkuluku.")
            break
    else:
      print("se on alkuluku.")