# Kristijan Kačan, 4.12.2017.

# Vježba 5 zadatak 5

# unos niza znakova
niz=str(input("Unesite niz znakova: "))

i=0
while i<len(niz):
    if (niz[i].lower().isalpha()):
        if (niz[i:i+2].lower()=="lj" or niz[i:i+2].lower()=="nj" or niz[i:i+2].lower()=="dž"):
            print(niz[i:i+2])
            i+=2
        else:    
            print(niz[i])
            i+=1
    else:
        i+=1
