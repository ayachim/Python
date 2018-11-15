#convert hexa & deci
nombre=input()

H="0123456789ABCDEF"
T=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
som=0
T1=0
loop=0
for i in nombre:
    print(i,loop)
    T1=int(T[H.index(i)])
    som = som+(T1*16**loop)
    loop=loop+1
print(som)
