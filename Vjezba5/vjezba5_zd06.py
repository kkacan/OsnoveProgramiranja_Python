# Kristijan Kačan, 4.12.2017.

# Vježba 5 zadatak 6

# unos broja ocjena
n=int(input("Unesite broj ocjena: "))

lista_ocjena=list(range(1,n+1))

i=0
while i<len(lista_ocjena):
   ocjena=int(input("Unesite {}. ocjenu od 1 do 5: ".format(lista_ocjena[i])))
   if (0<ocjena<6):
       lista_ocjena[i]=ocjena
       i+=1
   else:
       print("Neispravan unos! Ocjena mora biti od 1 do 5")

if ("1" in lista_ocjena):
    print("Nedovoljan")
else:
    zbroj=0
    for i in range (0,len(lista_ocjena)):
       zbroj+=int(lista_ocjena[i]) 
    print("Prosjek ocjena je:",zbroj/n)
