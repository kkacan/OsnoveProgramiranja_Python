# Kristijan Kačan, 4.12.2017.

# Vježba 5 zadatak 4

# unos niza znakova
niz=str(input("Unesite niz znakova: "))

for i in range (0, len(niz)):
    if (niz[i].lower().isalpha() and niz[i].lower()!="č" and niz[i].lower()!="ć"
        and niz[i].lower()!="ž" and niz[i].lower()!="đ" and niz[i].lower()!="š"):
        print(niz[i])

