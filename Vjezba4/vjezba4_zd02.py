# Kristijan Kačan, 16.11.2017.

# Vježba 4 zadatak 2

# unos dva niza znakova
niz1=input("Unesi prvi niz znakova: ")
niz2=input("Unesi drugi niz znakova: ")

# provjera da li se prvi niz nalazi unutar drugog
if niz1 in niz2:
    print("Niz","'"+niz1+"'","nalazi se unutar niza","'"+niz2+"'")
else:
    print("Niz","'"+niz1+"'","ne nalazi se unutar niza","'"+niz2+"'")
