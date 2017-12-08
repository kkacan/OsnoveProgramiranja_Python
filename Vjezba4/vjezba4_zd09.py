# Kristijan Kačan, 16.11.2017.

# Vježba 4 zadatak 9

# unos niza znakova
niz=str(input("Unesite proizvoljan niz znakova: "))
# kreiranje liste
lista=list(niz)

# pretraga koliko se praznina nalazi u listi i ispis
print("U listi se pojavljuje praznina",lista.count(" "),"puta")

# sortiranje liste uzlazno
lista.sort()

# brisanje zadnjeg znaka liste i ispis
del lista[-1]
print(lista)

# izbacivjanje prvog pojavljivanja slova 'a' iz liste i ispis
if lista.count("a")>0:
    lista.remove("a")
    print(lista)
else:
    print("Slovo 'a' se ne nalazi u listi")

