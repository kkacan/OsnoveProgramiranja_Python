#Kristijan Kačan Vježba 7 Zadatak 5

# unos niza znakova
niz=input("Unesite niz znakova: ")

# kreiranje liste
lista =list(niz)

# sortiranje liste
lista.sort()

# uklanjanje točaka i zareza
while "," in lista:
    lista.remove(",")
while "." in lista:
    lista.remove(".")

# ispis
print (lista)
