# Kristijan Kačan, 9.11.2017.
# Vježba 3 zadatak 1

# varijable x i y predstavljaju uređeni par kordinata

x= float(input("Unesite koordinatu x: "))
y= float(input("Unesite koordinatu y: "))

# provjera pozicije i ispis
if x==0 and y==0:
    print("Točka ({},{}) se nalazi u ishodištu kordinatnog sustava.".format(x,y))
elif x==0:
    print("Točka ({},{}) leži na y osi.".format(x,y))
elif y==0:
    print("Točka ({},{}) leži na x osi.".format(x,y))
elif x>0 and y>0:
    print("Točka ({},{}) nalazi se u I. kvadrantu.".format(x,y))
elif x<0 and y>0:
    print("Točka ({},{}) nalazi se u II. kvadrantu.".format(x,y))
elif x<0 and y<0:
    print("Točka ({},{}) nalazi se u III. kvadrantu.".format(x,y))
else: 
    print("Točka ({},{}) nalazi se u IV. kvadrantu.".format(x,y))     
