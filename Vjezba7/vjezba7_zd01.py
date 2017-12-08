#Kristijan Kačan Vježba 7 Zadatak 1

from math import *

a=int(input("Unesite dužinu stranice kvadrata a: "))

if a>0:
    print ("Površina kvadrata je", a**2)
    print ("Diagonala kvadrata je ",a*sqrt(2))
else:
    print ("Broj",a, "je manji od 1")

