# Kristijan Kačan, 30.11.2017.
# Vježba 6 zadatak 5


# unos niza znakova
niz=str(input("Unesite niz znakova: "))
# kreiranje liste
lista=list(niz)
# brisanje zadnjeg znaka
lista[:-1]
# dodavanje znaka + na kraj liste
lista.append("+")
# sortiranje liste
lista.sort()
# pretvaranje liste u string
string=str("".join(lista))
# ispis
print(string)
