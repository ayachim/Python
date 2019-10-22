#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
 nom: KOYUNCU BENNOUAR AYACHI
 date: 20/10/2019
 version: 1
 Livrable Chapitre 1 : La recette des crêpes
"""

# Module pour nous permettre de quitter le programme suite à une mauvaise saisie
import sys

try :
    # Variable pour le nombre personnes
    nombreDePersonnes = int(input("Saisir le nombre de personnes : "))
except ValueError :
    print("Valeur non correcte. Sortie...")
    sys.exit(-1)

if nombreDePersonnes <= 0 :
    print("Veuillez entrer une valeur supérieure à 0. Sortie...")
    sys.exit(-1)

# Quantité de farine
farine = int((250*nombreDePersonnes)/8)

# Nombre d'oeufs
oeufs = int((4*nombreDePersonnes)/8)

# Quantité de lait
lait = int((50*nombreDePersonnes)/8)

# Quantité de beurre
beurre = int((50*nombreDePersonnes)/8)

# Quantité de sucre vanillé
sucre = int((10*nombreDePersonnes)/8)

# Quantité de rhum
rhum = int((5*nombreDePersonnes)/8)

#Affichage
print("Pour", nombreDePersonnes, "personnes il faut :")
print(farine, "g de farine")
print(oeufs, "oeufs")
print(lait, "cl de lait")
print("1 pincée de sel")
print(beurre, "g de beurre")
print(sucre, "g de sucre vanillé")
print(rhum, "cl de rhum")