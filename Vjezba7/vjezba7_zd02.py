#Kristijan Kačan Vježba 7 Zadatak 2


k=int(input("Unesite prirodni broj: "))

i=1
j=1
brojevi=""
if k>0:
    while i<k:
        j+=1
        if j%2==0 and (j%3==0 or j%5==0):
            i+=1
            brojevi+=str(j)
    print(brojevi)

else:
    print("Broj je manji od 1")
