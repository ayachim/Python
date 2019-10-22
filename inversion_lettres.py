#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Date : ....
Auteur : ...
Version : V1
Thème du script : ...
'''



def calcDiesel(km,dur):
    return (km*0.1 + dur*50)

def calcEssence(km,dur):
    return (km*0.15 + dur*40)




try:

    distance=int(input())
    duree=int(input())

except:
    print("Saisir un nombre entier svp")

print("Pour",duree,"jours et",distance,"km")


if(calcDiesel(distance,duree) > calcEssence(distance,duree)):
   print("avec un véhicule à essence :",calcEssence(distance,duree))
   print("avec un véhicule diesel :",calcDiesel(distance,duree))
   print("Véhicule à essence conseillé")



elif(calcDiesel(distance,duree) < calcEssence(distance,duree)):
   print("avec un véhicule à essence :",calcEssence(distance,duree))
   print("avec un véhicule diesel :",calcDiesel(distance,duree))
   print("Véhicule diesel conseillé")

else:

   print("avec un véhicule à essence :",calcEssence(distance,duree))
   print("avec un véhicule diesel :",calcDiesel(distance,duree))
   print("Véhicule diesel et essence au même prix")
