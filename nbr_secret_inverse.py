#le nombre secret inverse

nbmin=int(input("Saisir le nombre minimal"))
nbmax=int(input("Saisir le nombre maximal"))
pari=""
verif=False


delta=(nbmax-nbmin)/2
resultat=delta
while(not verif):

    print("Le nombre secret est :",abs(resultat)," ?")
    pari=input("saisir egale, plus ou moins")

    while (pari=="p"):
        median1=round((resultat+nbmax)//2)
        print("Le nombre secret est :",abs(median1)," ?")
        pari=input("saisir egale, plus ou moins")
        median1=round((median1+nbmax)//2)
        

    while (pari=="m"):
        resultat=round((nbmax+resultat)/2)
        print("Le nombre secret est :",abs(resultat)," ?")

        pari=input("saisir egale, plus ou moins")


   
