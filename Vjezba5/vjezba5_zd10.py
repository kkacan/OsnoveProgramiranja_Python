# Kristijan Kačan, 4.12.2017.

# Vježba 5 zadatak 10

# unos prirodnog broja

n=int(input("Unesite prirodni broj: "))

brojac=n
while brojac>0:
    lista=(list(str(brojac)))
    if (lista==lista[::-1]):
        print("Broj",brojac,"je prvi manji broj od",n," koji je palindrom")
        brojac=0
    brojac-=1
