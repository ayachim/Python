# perimetre et algorithme

aire=0
longueur=0
largeur=0
perimetre=0

verif=True

while verif:

    print("Saisir la longueur du rectangle, nombre entier positif : ")
    longueur=input()
    
    print("Saisir la largeur du rectangle, nombre entier positif : ")
    largeur=input()
    print(largeur,longueur)

    #if (int(largeur) >= 0) or (int(longueur) >= 0):
    if longueur <=0:
        
    aire=int(longueur)*int(largeur)
    perimetre=(int(longueur)+int(largeur))*2
    verif=False

print("l'aire est : ",aire)
print("perimetre est : ",perimetre)
verif=False


