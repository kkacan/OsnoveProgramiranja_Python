# Kristijan Kačan, 9.11.2017.
# Vježba 3 zadatak 9


# unos slova
slovo=input("Unesite veliko ili malo slovo: ")

# projera da li je veliko ili malo slovo
if slovo.islower():
    
    print("Slovo je malo")
    print("Odgovarajući ASCII znak za slovo",slovo,"je", ord(slovo))
else:
    print("Slovo je veliko")
    print("Odgovarajući ASCII znak za slovo",slovo,"je", ord(slovo))
    

    
