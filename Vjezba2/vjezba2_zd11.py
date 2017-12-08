# Kristijan Kačan Vježba2 zadatak11 21.11.2017.


import cmath

# unos variabli a,b,c
a=int(input("Unesi koeficijent a: "))
b=int(input("Unesi koeficijent b: "))
c=int(input("Unesi koeficijent c: "))

# izračun rješenja
x1=((-b+cmath.sqrt((b**2)-(4*a*c)))/(2*a))
x2 =((-b-cmath.sqrt((b**2)-(4*a*c)))/(2*a))

# ispis rješenja
print("Rješenja kvadratne jednadžbe", a, "x^2+", b, "x+", c, "=0 su:{:.2f} i {:.2f}".format(x1, x2))









