#Kristijan Kačan Vježba 9 zadatak 1

def kompresija_teksta():

    ulazni_string=str(input("Unesite string znakova: "))
    lista=list(ulazni_string)
    izlazna_lista=[]
    broj_znakova=0
    i=0
    j=0

    while i<len(lista):
        znak=lista[i]
        if j==len(lista): j=i
        i+=1

        while j<len(lista):
            if znak==lista[j]:
                broj_znakova+=1    
                j+=1
                if j==len(lista):
                    izlazna_lista.append(znak)
                    if broj_znakova>1:
                        izlazna_lista.append(str(broj_znakova))
                    i=len(lista)
            else:
                izlazna_lista.append(znak)
                if broj_znakova>1:
                    izlazna_lista.append(str(broj_znakova))
                broj_znakova=0
                i=j
                j=len(lista)

    komprimirani_string=str("".join(izlazna_lista))  
    #print("Komprimirani string: ",komprimirani_string)
    return komprimirani_string

def dekompresija_teksta():
    ulazni_string=str(input("Unesite komprimirani string znakova: "))
    lista=list(ulazni_string)
    izlazna_lista=[]
    broj_znakova=0

    for i in range (0, len(lista)):
        znak=lista[i]
        
        if not znak.isdigit():
            izlazna_lista.append(znak)
        else:
            for j in range(0,int(lista[i])-1):
                izlazna_lista.append(lista[i-1])
                
    dekomprimirani_string=str("".join(izlazna_lista))
    #print("Dekomprimirani string: ",dekomprimirani_string)
    return dekomprimirani_string

print("Komprimirani string: ",kompresija_teksta())
print("Dekomprimirani string: ",dekompresija_teksta())

