# Kristijan Kačan, 30.11.2017.
# Vježba 6 zadatak 2


#unos broja

n=int(input("Unesite prirodni broj: "))
brojac=0
i=1

if n>0:
    
    while brojac<n:
    
       if i%2==0:
          print(str(brojac+1)+".","Broj",i,"je djeljiv sa 2")
          brojac+=1
       if i%3==0:
          print(str(brojac+1)+".","Broj",i,"je djeljiv sa 3")
          brojac+=1
       i+=1
     
else:
    print ("Broj je manji od 1")
