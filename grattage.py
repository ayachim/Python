#grattage au loto
import random
loto=[]
total=0
while total<5:

    for i in range(0,4):
        loto.append(random.randint(1,5))
        print(loto[i])
        
    if (sum(loto)%2)==0:
        print("t-as gagné 1 euro")
        total=1
    elif (max(loto)==2):
        print("t'as gagné 2 euros")
        total=2+total
    elif (loto.count(2)>=3):
          print("compteur :",loto.count(2))
          print("t'as gagné 5 euros")
          total = total+5

    else:
          print("tu gagnes rien")

    print(total)
      
