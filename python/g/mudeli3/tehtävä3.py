sukupuoli = input("anna sukupuolisen: ")
hemoglopiini = input("anna hemoglopiini: ")
if sukupuoli == "nainen" :
   if hemoglopiini <  "117":
      print("alhainen")
   elif hemoglopiini >  "175":
      print("korkea")
   elif  "117" <= hemoglopiini <= "175":
      print("normaali")
sukupuoli = input("anna sukupuolisen: ")
hemoglopiini = input("anna hemoglopiini: ")
if sukupuoli == "mies" :
   if hemoglopiini < "134":
      print("alhainen")
   elif hemoglopiini > "195":
      print("korkea")
   elif  "134" <= hemoglopiini <= "195":
      print("normaali")