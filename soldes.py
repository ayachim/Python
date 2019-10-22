#!/bin/python3
# -*- coding: utf-8 -*-
"""
Nom : AYACHI
Date : 12/10/19
version : 1
objet : exercice soldes

"""
prixArticle=input()

pourcentReduc=input()

 

print("Pour un article a un prix initial de",prixArticle,"€ et soldé a",pourcentReduc,"% :")

print("Le montant de la raduction est",round(prixArticle*(pourcentReduc/100),2),"€.")

print("Le prix solde est", round(prixArticle-(prixArticle*(pourcentReduc/100)),1),"€.")
