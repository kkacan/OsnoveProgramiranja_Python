# Kristijan Kačan, 16.11.2017.

# Vježba 4 zadatak 11

# unos imena i dodavanje u listu
lista=list(input("Unesite proizvoljan niz znakova A, B i C: "))

# izračun postotka i ispis
slovo_a=lista.count("A")
slovo_b=lista.count("B")
slovo_c=lista.count("C")

print("Slovo 'A' ima udio {:.2f}%".format(100/(len(lista))*slovo_a), sep="")
print("Slovo 'B' ima udio {:.2f}%".format(100/(len(lista))*slovo_b), sep="")
print("Slovo 'C' ima udio {:.2f}%".format(100/(len(lista))*slovo_c), sep="")

lista.sort()
print(lista)




