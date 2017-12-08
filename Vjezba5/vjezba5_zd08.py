# Kristijan Kačan, 4.12.2017.

# Vježba 5 zadatak 8

# unos broja u sustavu sa bazom 5
n=input("Unesite broj u sustavu sa bazom 5 (od 0 do 4): ")

broj_baza_5=True
for i in range(0,len(n)):
    if int(n[i])<0 or int(n[i])>4 : broj_baza_5=False
    
if broj_baza_5:
    print("Broj",n,"u dekadskom obliku iznosi:",int(str(n),5))
else:
    print("Broj nije u sustavu sa bazom 5")
