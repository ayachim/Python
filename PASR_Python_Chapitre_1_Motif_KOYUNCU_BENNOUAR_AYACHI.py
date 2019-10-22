#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
 nom: KOYUNCU BENNOUAR AYACHI
 date: 20/10/2019
 version: 1
 Livrable Chapitre 1 : Le motif Python dessiné avec un caractère quelconque
"""
# Module pour nous permettre de quitter le programme suite à une mauvaise saisie
import sys

# Motif a repeter
caractere = str(input("Saisir un caractere : "))

if len(caractere) != 1 :
    print("Entrez un seul caractère. Sortie...")
    sys.exit(-1)

# Version avec des ','
# Affichage
print(caractere*4, "",  caractere, " ", caractere, "", caractere*5, "", caractere, " ", caractere, "", caractere*5, "", caractere, " ", caractere)
print(caractere, "", caractere, " ", caractere, caractere, "   ", caractere, "  ", caractere, " ",caractere, "", caractere, " ", caractere, "",caractere*2,"", caractere)
print(caractere*4, " "*2, caractere, " "*4, caractere, " "*2, caractere*5, "", caractere, " ", caractere, "", caractere,caractere,caractere)
print(caractere, " "*5, caractere, " "*4,caractere, " "*2, caractere, " ", caractere, "", caractere, " ", caractere, "", caractere, "", caractere*2)
print(caractere, " "*5, caractere, " "*4,caractere, " "*2, caractere, " ", caractere, "", caractere*5, "", caractere, " ", caractere)

""" Version avec des '+'
print(caractere*4 + " "*2 + caractere + " "*3 + caractere + " "*2 + caractere*5 +  " "*2 + caractere + " "*3 + caractere + " "*2 + caractere*5 + " "*2 + caractere + " "*3 + caractere)
print(caractere + " "*2 + caractere + " "*3 + caractere + " " + caractere + " "*5 + caractere + " "*4 + caractere + " "*3 + caractere + " "*2 + caractere + " "*3 + caractere + " "*2 + caractere*2 + " "*2 + caractere)
print(caractere*4 + " "*4 + caractere + " "*6 + caractere + " "*4 + caractere*5 + " "*2 + caractere + " "*3 + caractere + " "*2 + caractere + " " + caractere + " " + caractere)
print(caractere + " "*7 + caractere + " "*6 + caractere + " "*4 + caractere +  " "*3 + caractere + " "*2 + caractere + " "*3 + caractere + " "*2 + caractere + " "*2 + caractere*2)
print(caractere + " "*7 + caractere + " "*6 + caractere + " "*4 + caractere +  " "*3 + caractere + " "*2 + caractere*5 + " "*2 + caractere + " "*3 + caractere)
"""