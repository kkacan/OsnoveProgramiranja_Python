#Kristijan Kačan Vježba 9 zadatak 3

def spoji_liste(l, k):

    l.extend(k)

    for i in range(0, len(l)):
        for j in range(1, len(l)-i):
            if str(l[j-1])>str(l[j]):
                (l[j-1],l[j])=(l[j],l[j-1])
        
    print(l)

n=int(input("Unsesite broj n: "))

if n>0:

    i=0
    j=0
    lista1=[]
    lista2=[]

    while i<n:
        i+=1
        string1=str(input("Unsesite {}. znak prve liste: ".format(i)))
        lista1.append(string1)
    
    while j<n:
    
        j+=1
        string2=str(input("Unsesite {}. znak druge liste: ".format(j)))
        lista2.append(string2)

    lista1.sort()
    print (lista1)
    lista2.sort()
    print (lista2)
    
    spoji_liste(lista1,lista2)
else:
    print("Broj",n,"nije veći od nule!")
    
    
