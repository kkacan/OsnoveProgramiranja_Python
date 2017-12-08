# Kristijan Kačan, 23.11.2017.
# Vježba 5 zadatak 1

#unos broja
n=int(input("Unesite prirodan broj: "))
#ispis prvih n prirodnih brojeva
print ("a) Prvih n prirodnih brojeva: ", end=" ")
for i in range(n):
    print(i+1, end=" ")

"""
i=1

while i<=n :
    print (i, end=" ")
    i+=1
    
"""
print()#print u novom redu

#ispis prvih n neparnih brojeva
print ("b) Prvih n neparnih brojeva: ", end=" ")
for i in range(n):
    print(2*i+1, end=" ")
print()

#ispis prvih n faktorijela
faktorijele=1
print ("c) n-faktorijela: ", end=" ")
for i in range(1,n+1):
    faktorijele*=i
    
print(faktorijele)

# ispis parnih/neparnih manjih od n
print("d) ispis svih parnih/neparnih")
if n%2==1:
    for i in range (1,n+1):
        if i%2==1: print (i,end=" ")
else:
    for i in range (1,int(n/2+1)):
        print(2*i, end=" ")
        
    


            

