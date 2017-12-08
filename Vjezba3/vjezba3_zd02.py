# Kristijan Kačan, 9.11.2017.
# Vježba 3 zadatak 2


from math import sqrt

# varijable a,b i c predstavljaju duljine stranica trokuta

a= float(input("Unesite duljinu stranice a: "))
b= float(input("Unesite duljinu stranice b: "))
c= float(input("Unesite duljinu stranice c: "))

# provjeravamo da li te stranice sačinjavaju trokut i izračunamo površinu

if a+b>c and a+c>b and b+c>a:
    
    s=(a+b+c)/2
    p=sqrt(s*(s-a)*(s-b)*(s-c))
    print("Površina trokuta je ",p)
    
else:

    print("Ovo nije trokut")
    

    
