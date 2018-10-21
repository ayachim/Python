#aire et perimetre

print("saisir la largeur et la longueur votre rectangle")

long=int(input())
large=int(input())

if (long*large)==0:
    print("saisir 2  nombre sitrictement positif")
    long=int(input())
    large=int(input())
    
else:
    print("le perimetre est de :",(long+large)*2," m")
    print("l'aire est de :",long*large," m²")
