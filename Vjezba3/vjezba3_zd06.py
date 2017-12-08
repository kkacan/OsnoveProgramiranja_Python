# Kristijan Kačan, 23.11.2017.
# Vježba 3 zadatak 6

#unos cijelog broja
broj=int(input("Unesite cijeli broj: "))

#unos baze
baza=int(input("Unesite bazu: "))

if baza==2:
    print ("Broj",broj, "u binarnom obliku iznosi:", bin(broj))
elif baza==8:
    print ("Broj",broj, "u oktalnom obliku iznosi:", oct(broj))
elif baza==16:
    print ("Broj",broj, "u heksadecimalnom obliku iznosi:", hex(broj))
else:
    print ("Baza nije dobro unesena")
