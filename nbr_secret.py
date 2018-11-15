#le nombre secret
from random import *
#variables
hasard=int(randint(1,10000))
pari=int(input("Donner un nombre pour trouver le nombre secret"))
count=1
trouve=False
while (hasard != pari):
    if (pari>hasard):
        print("trop haut")
        pari=int(input("Rejouez"))

    elif (pari<hasard):
        print("trop bas")
        pari=int(input("Rejouez"))
    count=count+1
    if (count>14):
        break

if(trouve):
    print("Bravo! Vous avez trouver en ,",count," fois" )

else:
    print("Dommage, vous avez eu ",count," chance sans trouver" )
