# Kristijan Kačan, 23.11.2017.
# Vježba 5 zadatak 2

#unos broja
n=int(input("Unesite prirodan broj: "))

brojac=0
if n<1:
    print("unos mora biti veći od 0")
else:
    
    for i in range (1, n+1):
        if n%i==0:
            print(i)
            brojac+=1

        if brojac==1:
            print ("Broj 1 nije prost ni slozen)ž")
        elif brojac==2:
            print ("boj",n,"je prost")
        else:
            print ("broj",n,"je slozen i ima",brojac, "djelitelja")

        
    


            

