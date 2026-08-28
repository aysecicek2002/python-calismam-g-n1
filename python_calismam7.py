# BREAK CONTINUE KULLANIMI
"""
for sayi in range(1,11):
    if sayi==5:
        print("dongu break komutuyla sonlandirildi")
        break
    print(sayi)
    #burada break komutu 5 e kadar olan sayilari yazabildi. cünkü dongu sonlandirildi.

for sayi2 in range(2,24):
    if sayi2%2==1:
        continue
    print(sayi2) #yani tek sayılara geldiginde onlari alma ama donguye devam et
"""

    #RANDOM MODULU ILE RANDINT KULLANIMI VE SHUFFLE KULLANIMI
import random
sayi= random.randint(0,100)#random sayi atar
print(sayi)
#shuffle(list) verilen listeyi karıştırır
liste=["ahmet","ayse","mehmet","beyza","yaren","yemliha"]
random.shuffle(liste)
print("karistirilmis liste: ",liste)


from random import randint #from kullarak aslında randiti sabitledik ve hr defasinda yazmaktan kurtulduk
sayi2=randint(200,300)
print(sayi2)
  
from random import shuffle #from kullarak aslında shuffle ı sabitledik ve hr defasinda yazmaktan kurtulduk
kelimeler=["ayse","gokdeniz","python","ogreniyorum"]
shuffle(kelimeler)
print(kelimeler)

