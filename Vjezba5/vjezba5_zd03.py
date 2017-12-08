# Kristijan Kačan, 4.12.2017.

# Vježba 5 zadatak 3

# unos brojeva m i n
n=int(input("Unesite prvi broj: "))
m=int(input("Unesite drugi broj: "))

najveci_djelitelj=0
if m>0 and m>0:
    if m>n:
        for i in range (1,m):
            if m%i==0 and n%i==0:
                najveci_djelitelj=i
                
    else:
        for i in range (1,n):
            if m%i==0 and n%i==0:
                najveci_djelitelj=i

    print("Najveći djelitelj brojeva",n,"i",m,"je",najveci_djelitelj)

else:
    print("Brojevi nisu veći od nule")
