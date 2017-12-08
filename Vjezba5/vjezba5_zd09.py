# Kristijan Kačan, 4.12.2017.

# Vježba 5 zadatak 9

# unos dva prirodna broja
m=int(input("Unesite prvi prirodni broj: "))
n=int(input("Unesite drugi prirodni broj: "))

brojac=0
if m>n:
    for i in range (n+1,m):
        lista=list(str(i))
        zbroj=0
        
        for j in range (0,len(lista)):
            zbroj+=int(lista[j])
        if zbroj==10:
            brojac+=1
            print ("Broju",i,"je zbroj znamenaka jednak 10")
    if brojac<1: print("Imeđu brojeva",n,"i",m,"nema broja čiji je zbroj znamenaka jednak 10")

elif n>m:        
    for i in range (m+1,n):
        lista=list(str(i))
        zbroj=0
        
        for j in range (0,len(lista)):
            zbroj+=int(lista[j])
        if zbroj==10:
            brojac+=1
            print ("Broju",i,"je zbroj znamenaka jednak 10")
    if brojac<1: print("Imeđu brojeva",m,"i",n,"nema broja čiji je zbroj znamenaka jednak 10")       


else:
    print("Brojevi su jednaki")
