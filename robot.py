#!/usr/bin/env python3.5

#robot qui traverse en fonction des couleurs des feux
#verifier si voie libre

couleur_rouge="rouge"
couleur_orange="orange"
couleur_verte="vert"
couleur=""

print("De quelle couleur est le feu? (rouge, vert, orange")
couleur=input()
if couleur_rouge=="rouge" or couleur_orange=="orange" or couleur_verte=="vert":

    if couleur == couleur_rouge:
        print("le feu est rouge, stop !")

            
    if couleur == couleur_verte:
        
        print("le feu est vert, la voix est libre, passe !")
        

    elif couleur == couleur_orange:
        print("le feu est orange")

    else:
        print("probleme d'orthographe !")
