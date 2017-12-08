# Kristijan Kačan, 9.11.2017.
# Vježba 3 zadatak 5


import math


# unos variabli a,b,c
a=int(input("Unesi koeficijent a: "))
b=int(input("Unesi koeficijent b: "))
c=int(input("Unesi koeficijent c: "))

if a==0:
    print("Ovo nije kvadratna jednadžba")
else:

    # izračun rješenja
    D=((b**2)-(4*a*c))
    if D<0:
        print("Nema realnih rješenja")
    elif D>0:
        x1=((-b+math.sqrt(D))/(2*a))
        x2 =((-b-math.sqrt(D))/(2*a))
        # ispis rješenja
        print("Rješenja kvadratne jednadžbe za koeficijent a =", a, "koeficjent b =", b, "i koeficijent c =", c, "su:{:.2f} i {:.2f}".format(x1, x2))
    else:
        x1=((-b+cmath.sqrt(D))/(2*a))
        print("Rješenje kvadratne jednadžbe za koeficijent a =", a, "koeficjent b =", b, "i koeficijent c =", c, "je:{:.2f}".format(x1))

    

    

    
