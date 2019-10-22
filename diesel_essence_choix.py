#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Date : ....
Auteur : ...
Version : V1
Thème du script : ...
'''


def minToMaj(num):
        return num+32

def majToMin(num):
        return num-32

try:
    number=ord(str(input()))



    if(number >= 97 and number <= 122):
        #fonction maj to min
        print("Vous avez saisi la lettre minuscule",chr(number)+".")
        print("Après transformation en majuscule, on obtient la lettre",chr(majToMin(number))+".")


    elif(number >= 65 and number <= 90):
        #fonction min to maj
        print("Vous avez saisi la lettre majuscule",chr(number)+".")
        print("Après transformation en minuscule, on obtient la lettre",chr(minToMaj(number))+".")

    else:
        print("Vous avez saisi le caractère "+chr(number)+", ce n'est pas une lettre.")


except:
    print("Une seule lettre svp ! ! ")
