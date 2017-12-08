# Kristijan Kačan, 9.11.2017.
# Vježba 3 zadatak 7

import math


# unos argumenta i baze

argument= int(input("Unesite argument: "))
baza= int(input("Unesite bazu: "))


if baza >1 and argument>0:
    
    print("Logaritam od", argument,"i baze",baza,"je",math.log(argument, baza))
else:
    print ("Vrijednosti argumenta i baze nisu dobro unesene")
    

    
