#1. Tekur inn t�lu sem �kve�ur hversu margar t�lur eru prenta�ar
#2. Skilgreinir t�lu 1 og t�lu 2
#3. for-loopa er byrju�
#4. Ef tala 1 er 0, er h�n gefin t�lu j�fn og i, ef tala 2 er 0, er h�n gefin gildi af i+1 
#5. Ef tala 1 og 2 hafa gildi, tala 3 er j�fn og tala 1 og 2 summu�
#6. Tala 3 er ger� a� t�lu 2 og 2 a� 1
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
