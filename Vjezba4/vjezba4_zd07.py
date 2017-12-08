# Kristijan Kačan, 16.11.2017.

# Vježba 4 zadatak 7

# unos niza znakova
n=int(input("Unesite cijeli broj veći od 1: "))

# provjera da li je broj veći od 1 i ispis
if n>1:
    print(list(range(1,n+1)))
    
    lista=list(range(2,(2*n)+1,2))
    lista.reverse()
    print(lista)
else:
    print ("Broj",n,"nije veći od 1")

