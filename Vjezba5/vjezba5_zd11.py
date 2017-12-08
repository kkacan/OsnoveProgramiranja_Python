# Kristijan Kačan, 4.12.2017.

# Vježba 5 zadatak 11

# unos niza znakova

niz=input("Unesite niz znakova: ")

lista=list(niz)
lista_sifr=[]
lista_sifr_ispis=[]

for i in range(0,len(lista)):
    lista_sifr.append(ord(lista[i])+1)

for j in range(0,len(lista_sifr)):
    lista_sifr_ispis.append(chr(lista_sifr[j]))
    
print ("Šifrirani niz od znakova",niz,"je:","".join(lista_sifr_ispis))
