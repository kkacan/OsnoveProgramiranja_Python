# Kristijan Kačan, 5.11.2017.
# Vježba2 zadatak 3


# definicija variable za unos centimetara
cm=float(input("Upiši centimetre: "))

# definicija variable stopa i izračun vrijednosti u centrimetrima
stopa= int(cm//30.48)

# definicija variable otatak i izračun ostatka u centrimetrima
ostatak= cm%30.48

# definicija variable inča i izračun vrijednosti u centrimetrima
inca=int(ostatak//2.54)

# ispis rezultata
print ("Duljina od", cm ,"cm odgovara duljini od" ,stopa, "stopa i" ,inca,"inča")

