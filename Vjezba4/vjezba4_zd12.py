# Kristijan Kačan, 16.11.2017.

# Vježba 4 zadatak 12

# unos niza znamenaka
lista=list(input("Unesite niz znamenaka: "))

# izračun aritmetičke sredine i ispis
zbroj=0
for i in range (0, len(lista)-1):
    zbroj+=int(lista[i])
sredina=zbroj/len(lista)
print("Aritmetička sredina zanamenaka",lista,"iznosi:",sredina)




