# Kristijan Kačan, 30.11.2017.
# Vježba 6 zadatak 1

import math

# unos decimalnog broja
a=float(input("Unesite decimalni broj: "))

# provjera da li je broj veći od 0 izračun i ispis
if a>0:
    P=(((a**2)*math.sqrt(3))/4)
    print("Površina jednakostraničnog trokuta duljune stranice",a,"iznosi {:.2f}".format(P))
else:
    print ("Broj je manji od nule")
