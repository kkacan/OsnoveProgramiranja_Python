# Kristijan Kačan, 16.11.2017.

# Vježba 4 zadatak 8

# unos cijelog broja 
n=int(input("Unesite cijeli broj veći od 1: "))

# provjera da li je broj veći od 1
if n>1:
    # kriranje liste parnih brojeva i ispis
    lista_parnih_brojeva=list(range(2,n,2))
    print(lista_parnih_brojeva)
    # kreiranje liste neparnih brojeva i ispis
    lista_neparnih_brojeva=list(range(1,n,2))
    print(lista_neparnih_brojeva)
    # kriranje nove liste i ispis
    nova_lista=lista_parnih_brojeva+lista_neparnih_brojeva
    print(nova_lista)
    # sortiranje liste uzlazno i ispis
    nova_lista.sort()
    print(nova_lista)
else:
    print("Broj",n,"nije veći od 1")
