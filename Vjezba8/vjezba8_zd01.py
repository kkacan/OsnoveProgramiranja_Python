#Kristijan Kačan Vjezba8 zadatak 1 11.1.2018.

import math

# a)    
def zbroj(x,y):
    return(x+y)
# b) 
def zbroj_znamenaka(n):
    lista=(list(str(n)))
    zbroj=0
    for i in range(0, len(lista)):
        zbroj+=int(lista[i])
    return zbroj
# c) 
def udaljenost_od_0(x,y):
    return (math.sqrt(x**2+y**2))

# d)
def udaljenost_tocaka(x_1,y_1,x_2,y_2):
    return(math.sqrt(((x_1-x_2)**2)+((y_1-y_2)**2)))
    


