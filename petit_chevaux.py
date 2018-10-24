#jeu des petit chevaux
import random
#random.seed(10)
count= 0
tirage=False

while not tirage:
    r=random.randint(0,6)
    print(r)
    count = count+1
    if r == 6:
        tirage=True
        
print("Trouvé en :",count ,"fois")
        

    
