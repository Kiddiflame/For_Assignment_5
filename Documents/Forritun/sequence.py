#1. Tekur inn tölu sem ákveður hversu margar tölur eru prentaðar
#2. Skilgreinir tölu 1 og tölu 2
#3. for-loopa er byrjuð
#4. Ef tala 1 er 0, er hún gefin tölu jöfn og i, ef tala 2 er 0, er hún gefin gildi af i+1 
#5. Ef tala 1 og 2 hafa gildi, tala 3 er jöfn og tala 1 og 2 summuð
#6. Tala 3 er gerð að tölu 2 og 2 að 1
#7 Endurtaka skref 5 og 6


n = int(input("Enter the length of the sequence: ")) # Do not change this line
tala1 = 0
tala2 = 0
tala3 = 0

for i in range(1, n-1):
    if tala1 <= 0:
        tala1 = i
        tala2 = tala1+1
        tala3 = tala2+1
        print(tala1)
        print(tala2)
        print(tala3)
    else:
        tala4 = tala1+tala2+tala3
        tala1 = tala2
        tala2 = tala3
        tala3 = tala4
        print(tala4)
