# Kristijan Kačan, 23.11.2017.
# Vježba 3 zadatak 4

#unos bodova

bodovi=int(input("Unesite broj bodova od 0 do 100: "))

if 0<=bodovi<=100:

    if 0<=bodovi<=59:
        ocjena="1 (nedovoljan)"
    elif 60<=bodovi<=69:
        ocjena="2 (dovoljan)"
    elif 70<=bodovi<=79:
        ocjena="3 (dobar)"
    elif 80<=bodovi<=89:
        ocjena="4 (vrlo dobar)"
    elif 90<=bodovi<=100:
        ocjena="5 (izvrstan)"
    print("Ocijena za ove bodove je: "+ocjena)
else: print("Uneseni broj nije između 0 i 100")

