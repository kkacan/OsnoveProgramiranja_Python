# Kristijan Kačan 16.11.2017.
# Vježa 4 Zadatak 1

niz= input("Unesite niz znakova: ")

#a) ispiši duljinu
print("a) Duljina niza je ",len(niz))

#b) ispiši najveći element
print("b) Najveći element niza je ",max(niz))

#c) ispiši najmanji element
print("c) Najmanji element niza je ",min(niz))

#d) ispiši drugi znak niza
if len(niz) >= 2:
    print("d) Drugi znak niza je ",niz[1])
else:
    print("Niz nema dva elementa")

#e) ispiši zadnji znak niza
print("e) Zadnji znak niza je ",niz[-1])

#f) ispiši 3 puta
print("f) "+(niz+".")*2+niz)

#g) ispiši niz bez prvog i zadnjeg znaka
if len(niz) >= 2:
    print("g) "+niz[1:-1])
else:
    print()
    

#h) ispiši niz obrnutim redoslijedom
print("h) "+niz[::-1])

#i) ispiši svaki drugi znak niza
print("i) "+niz[::2])

#h) potraži slovo a u nizu i ispiši poziciju na kojoj se nalazi
if "a" in niz:
    print("j) Slovo a se pojavljuje na poziciji "+str(niz.index("a")+1))
else:
    print("Slovo a nije u zadanom nizu!")
    

