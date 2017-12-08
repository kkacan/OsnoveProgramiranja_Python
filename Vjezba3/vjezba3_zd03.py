# Kristijan Kačan, 9.11.2017.
# Vježba 3 zadatak 3



# unos dva cijela broja i računske operacije

a= int(input("Unesite cijeli broj a: "))
b= int(input("Unesite cijeli broj b: "))
c= input("Unesite računsku operaciju (+,-,* ili /): ")


# izračun i ispis

if c=="+" :
  
    print(a,"+",b,"=",a+b)
    
elif c=="-" :
  
    print(a,"-",b,"=",a-b)

elif c=="*" :
  
    print(a,"*",b,"=",a*b)

elif c=="/" :
  
    print(a,"/",b,"=",a/b)     
    
else:

    print("Niste unijeli ispravnu računsku operaciju")
    

    
