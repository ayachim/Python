msg=input()
alphabet="abcdefghijklmnopqrstuvwxyz"
ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
stock=[0]*26
STOCK=[0]*26
tot=[0]*26
for i in msg:

    if (alphabet.count(i)>0): #or
        stock[alphabet.index(i)]=msg.count(i)

    if(ALPHABET.count(i)>0):
        stock[ALPHABET.index(i)]=msg.count(i)
        
for i in range(len(stock)):
    print(alphabet[i]," : ",stock[i]+STOCK[i]) 
    tot[i]=(stock[i]+STOCK[i])
    
print(alphabet[tot.index(max(tot))])
