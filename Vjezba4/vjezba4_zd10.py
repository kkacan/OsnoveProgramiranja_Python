# Kristijan Kačan, 16.11.2017.

# Vježba 4 zadatak 10

# unos imena i dodavanje u listu
lista=list()
ime=str(input("Unesite prvo ime: "))
lista.append(ime)
ime=str(input("Unesite drugo ime: "))
lista.append(ime)
ime=str(input("Unesite treće ime: "))
lista.append(ime)
ime=str(input("Unesite četvrto ime: "))
lista.append(ime)
ime=str(input("Unesite peto ime: "))
lista.append(ime)

#sortiranje liste uzlazno
lista.sort()

# ispis imena
for i in range (0,len(lista)):
    print(i+1,"."," ",lista[i],sep="")





