#!/#!/bin/python3
# -*- coding: utf-8 -*-

"""
Nom  : AYACHI
Date : 10/10/19
Version : 1
Object : Recette de creppes en fonction du nombre de personnes

"""
#variables :
farine = 250/8
oeuf = 4/8
lait = 50/8
sel = 1
beurre = 50/8
sucreV = 10/8
rhum = 5/8

#Demande de saisit
nbPersonne=int(input("Saisir le nombre de personne : " ))

#calculs et affichages
print("Pour",nbPersonne,"personnes il faut :")
print(int(farine*nbPersonne),"g de farine")
print(int(oeuf*nbPersonne),"oeufs")
print(int(lait*nbPersonne),"cl de lait")
print(sel,"pincee de sel")
print(int(beurre*nbPersonne),"g de beurre")
print(int(sucreV*nbPersonne),"g de sucre vanille")
print(int(rhum*nbPersonne),"cl de rhum")





