# Kristijan Kačan, 4.12.2017.

# Vježba 5 zadatak 7

# unos dvoznamenkastog broja
n=int(input("Unesite dvoznamenkasti prirodni broj: "))

if 9<n<100:
    lista=list(range(11,n,2))
    brojevi=""
    for i in range(0,len(lista)):
        if (int(str(lista[i])[::-1])%2!=0): brojevi+=str(lista[i])+","
    print("Neparni dvoznamenkasti brojevi manji od broja",n,"kada se čitaju sa lijeva na desno i obrnuto su:",brojevi[:-1])
else:
    print("Broj",n,"nije dvoznamenkast!")
