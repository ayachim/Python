#convertBintoHexa

nombre=input()

H="0123456789ABCDEF"
T=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]


print(nombre[-4:])
print(nombre[-len(nombre):-4])

for i in range(1,(len(nombre)//4)):
    #print(nombre[-4:])
    if (len(nombre)>4):
        print(nombre[-len(nombre)*i:-4])
