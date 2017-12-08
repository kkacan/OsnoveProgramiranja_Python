# Kristijan Kačan, 4.12.2017.

# Vježba 5 zadatak 12

# unos proizvoljnog broja pozitivnih brojeva

n=0
lista=[]
zbroj=0

while n>-1:
    n=int(input("Unesite broj: "))
    lista.append(n)

for i in range(0,len(lista)):
    zbroj+=lista[i]

print("Aritmetička sredina brojeva",lista,"iznosi:", zbroj/len(lista))
