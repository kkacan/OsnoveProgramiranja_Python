#Kristijan Kačan Vježba 7 Zadatak 4

niz=input("Unesite niz znakova: ")

#lista =niz.lower()
lista =list(niz.lower())

for i in range(0,len(lista)):
    if lista[i]=="č": lista[i]="c"
    if lista[i]=="ć": lista[i]="c"
    if lista[i]=="ž": lista[i]="z"
    if lista[i]=="š": lista[i]="s"
    if lista[i]=="đ": lista[i]="d"



print ("".join(lista))
