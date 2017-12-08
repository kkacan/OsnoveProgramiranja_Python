# Kristijan Kačan, 9.11.2017.
# Vježba 3 zadatak 10


# unos niza znakova
niz=input("Unesite niz od 5 znakova: ")

# provjera dužine niza
if len(niz)==5:

# definiranje varijabli i pridruživanje vrijednosti
    a=niz[0]
    b=niz[1]
    c=niz[2]
    d=niz[3]
    e=niz[4]

# provjera da li je niz palindrom
    if (a+b+c+d+e)==(e+d+c+b+a):
        print("Ova riječ je palindrom")
    else:
        print("Ova riječ nije palindrom")

# ispis memorijske lokacije    
    print("Adresa memorijske lokacije za znak",a,"je",id(a))
    print("Adresa memorijske lokacije za znak",b,"je",id(b))
    print("Adresa memorijske lokacije za znak",c,"je",id(c))
    print("Adresa memorijske lokacije za znak",d,"je",id(d))
    print("Adresa memorijske lokacije za znak",e,"je",id(e))
    
else:
    print("Ovaj niz nema 5 znakova")
    
