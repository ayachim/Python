nom=input()
prenom=input()
code=input()
service=""
travail="travail"
annee="20"+code[0:2]
numero=code[2:6]
sexe="Monsieur"
pronom="Il"
co=code[7]
if (code[6]==1):
    sexe="Madame"
    travail="travaille"
    pronom="Elle"
    
if (co=="0"):
    service="direction"
    
if (co=="1"):
    service="secretariat"
if (co=="2"):
    service="gestion"
if (co=="3"):
    service="informatique"
if (co=="4"):
    service="communication"
if (co=="5"):
    service="entretien"
if (co=="6"):
    service="fabrication"

print(co)

print(sexe,prenom,nom,travail, "au service",service,".",pronom,travail, "dans l'entreprise depuis", annee,"et son numéro d'embauche est le", numero,".") 
