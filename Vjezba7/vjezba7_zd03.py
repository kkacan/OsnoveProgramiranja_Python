#Kristijan Kačan Vježba 7 Zadatak 3

m=int(input("Unesite prvi cijeli broj: "))
n=int(input("Unesite drugi cijeli broj: "))

umnozak=1
if m<n:

    for i in range(m+1,n):
        umnozak*=i
    print("Umnožak svih brojeva između",m,"i",n,"iznosi",umnozak)
else:
    print("Broj",m,"je veći ili jednak od",n)
