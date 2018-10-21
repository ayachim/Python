#definir si les trois nombres saisit correspondent a un
#triangle rectangle ou ton
a=[]
print("Saisir les 3 cotés du triangle")
for i in range(3):
    a.append(input())
a.sort(reverse=True)

h=int(a[0])**2
b=int(a[1])**2
c=int(a[2])**2

if int(h) == int(b) + int(c):
    print("C'est un triangle rectangle !")
 

else:
    print("ce n'est pas un triangle rectangle")






















