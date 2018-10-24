#entraienement cycliste

#nbjour=21
distance=30
increment=10
cumul=0
#print("nbj : dst : cumul ") 
for r in range(21):    
    cumul=distance+cumul    
    #print(r+1,"   ", distance ," ",cumul) 
    if r == 6:
        print("----------------premiere semaine  :" ,cumul," km")
        sem1=distance        
    if r == 8:
        print("----------------au dixieme jour   :" ,distance," km")
    if r == 13:
        print("----------------deuxieme semaine  :" ,cumul,"km")
        sem2=cumul-(sem1)
    if r == 20:
        sem3=sem2+sem1
        print("----------------troisieme semaine :" ,cumul,"km")
    distance=distance+increment
print("----------------au derniere jour  :",distance," km")

