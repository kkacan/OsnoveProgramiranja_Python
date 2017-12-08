# Kristijan Kačan, 16.11.2017.

# Vježba 4 zadatak 6

# unos niza znakova
niz_1=str(input("Unesite prvi niz znakova: "))
niz_2=str(input("Unesite drugi niz znakova: "))

# provjera i ispis
if niz_1 in niz_2:
    print (niz_2[niz_2.find(niz_1)+len(niz_1):])
else:
    print("Niz",niz_1,"ne pojavljuje se u nizu",niz2)

