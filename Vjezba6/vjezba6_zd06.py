# Kristijan Kačan, 30.11.2017.
# Vježba 6 zadatak 6


#
import random

niz="abcd"
kombinacija=1
lista=list(niz)

for i in range(0,len(lista)):
    kombinacija*=len(lista)-i

i=0
lista_print=[]
lista_tmp=[]
while i<kombinacija:
    lista_tmp.append("".join(random.sample(lista, len(lista))))
    for j in range(0,len(lista_tmp)):
        if lista_tmp[j] not in lista_print:
            lista_print.append(lista_tmp[j])
            i+=1
lista_print.sort()
print(lista_print)

