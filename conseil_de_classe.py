#conseil_de_classe
import random
tbl = [0] * 30
tbl2 = []
tbl3 = []
#print(len(tbl))

for i in range(len(tbl)):
    #print("aa,",i,random.randint(0,20))
    #a=random.randint(0,20)
    #print(a)
    tbl[i]=random.randint(0,20)
    

a=sum(tbl)/len(tbl)
b=max(tbl)
c=min(tbl)
d=b-c
print("Moyenne : ",round(a,2))
print("Note max : ",round(b,2))
print("Note mini : ",round(c,2))
print("Etendue : ",round(d,2))

#calcul mediane

tbl.sort()

mediane=(tbl[15]-tbl[14])+tbl[14]
print("La mediane est de : ",mediane)

#calcul moyenne élaguée
tbl3 = tbl[1:29]
print("La moyenne élaguée est : ",round(sum(tbl3)/len(tbl3)))

for i in tbl:
    if tbl.index(i)<=10:
        #print(tbl.index(i))
        
        tbl2.append(tbl.index(i))
print("Nombre de note en dessous de 10/20 : ",len(tbl2))

