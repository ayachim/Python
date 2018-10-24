#mot de passe

mdp="password"
umdp=input("Votre mot de passe?")
count=0
while umdp != mdp:
    umdp=input("Votre mot de passe???!")    
    count=count+1
    print("vous reste ",count, "chances!")
    if count>=2:
        print("compte bloqué!!!!!!")
        break
print("Vous etes connecté")
