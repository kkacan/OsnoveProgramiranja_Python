# Kristijan Kačan, 16.11.2017.

# Vježba 4 zadatak 3

# unos niza znakova i cijelog broja
niz=str(input("Unesite niz znakova: "))
n=int(input("Unesite cijeli broj: "))

# provjera da li se nalazi unutar niza
if str(n+1) in niz:
    print("Broj",n+1,"se nalazi u nizu",niz)
else:
    print("Broj",n+1,"se ne nalazi u nizu",niz)
            

