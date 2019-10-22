#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
 nom: KOYUNCU BENNOUAR AYACHI
 date: 20/10/2019
 version: 1
 Livrable Chaptire 1 : Soldes
"""

# Module pour gérer les expressions régulières afin de vérifier la saisie du prix
import re
# Module pour nous permettre de quitter le programme suite à une mauvaise saisie
import sys

# Prix de l'article
try :
    prix = float(input("Saisir le prix de l'article : "))
except ValueError :
    print("Valeur non correcte. Sortie...")
    sys.exit(-1)

verifierPrix = str(prix)
if not re.search('^[0-9]*.?([0-9]){0,2}$', verifierPrix) :
    print("Veuillez saisir un bon prix (ex: 10.22)")
    sys.exit(-1)

# Réduction
try :
    reduction = int(input("Saisir le pourcentage de la réduction : "))
except ValueError :
    print("Valeur non correcte. Sortie...")
    sys.exit(-1)

# Montant de la réduction
montantDeLaReduction = int((prix*float(reduction/100))*100)/100

# Prix soldé
prixSolde = int(float(prix - montantDeLaReduction)*100)/100

# Affichage
print("Pour un article à un prix initial de", prix, "€ et soldé à", reduction, "% :")
print("Le montant de la réduction est", montantDeLaReduction, "€.")
print("Le prix soldé est", prixSolde, "€.")