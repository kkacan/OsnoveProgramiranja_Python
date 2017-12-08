# Kristijan Kačan, 30.11.2017.
# Vježba 6 zadatak 4


#unos niza znakova

niz=str(input("Unesite niz znakova: "))

lista=list(niz)

lista.reverse()
for i in range(0,len(lista)):
    if (lista[i]==","):
        lista.remove(",")
        lista.insert(i,".")
print ("".join(lista))

