# Kristijan Kačan, 30.11.2017.
# Vježba 6 zadatak 3


#unos dva prirodna broja

m=int(input("Unesite prirodni broj: "))
n=int(input("Unesite prirodni broj: "))

zajednicki_visekratnik=False
i=1

if n>0 and m>0:

    while zajednicki_visekratnik==False:
        if i%m==0 and i%n==0:
            print("Najmanji zajednički višekratnik brojeva",m,"i",n,"je",i)
            zajednicki_visekratnik=True
        i+=1
else:
    print("Uneseni brojevi nisu veći od nule!")
