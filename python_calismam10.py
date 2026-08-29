#STRING FONKSIYONLARI DETAYLI
"""metin="  MErhaba selamlar , dunya , NasilsiN , acaba , dunya  "
print(metin.upper()) #tum harflari buyuk yapar
print(metin.lower()) #tum harfleri kucuk yapar
print(metin.capitalize()) #en bastaki harf buyuk
print(metin.title()) #kelimelerin basindaki harf buyuk
print(metin.strip(),".") #o iki boslugu siler sağ ve sol
print(metin.lstrip(),".") #soldaki boslugu siler
print(metin.rstrip(),".") #sağdakini siler
print(metin.replace("dunya","world")) #belirtilen kelimeyle seçili kelimeyi degistirdik
print(metin.replace("dunya","world",1)) #secilen kelimeyi kac defa degistirmemiz gerektigini söylerç
print(metin.split()) #bosluğa göre liste yapar[merhaba,1,dunya,nasilsin,dunya]
print(metin.split(",")) #, e göre. [merhaba 1,dunya....]
liste=["ayse","fatma","cengiz"]
birlesik2=" () ".join(liste)  #output-> ayse : fatma : cengiz
print(birlesik2)  #ayse () fatma () cengiz
###############################3



#coklu atama [unpacking ya da destructuring] 

metin="104,ali,caliskan,11.sinif"
numara,ad,soyad,sinifi=metin.split(",")
print("numara:",numara,"\nad:",ad,"\nsoyad:",soyad,"\nsinif:",sinifi)


metin="selam ben ayse sen kimsin"
print(metin.find("fdgfdb")) #-1 doner boyle bı sey yok cunku
print(metin.find("e")) #0->s, 1->e
print(metin.find("s")) #0-> s var ilkini alir.
print(metin.find("fdgfdb"))
print(metin.index("selam"))  #find den farkli olarak olmayan bişi girersek value error verir  

"""

#
"""
string.isalpha() -> Tüm karakterler harf ise True, değilse False.
string.isdigit() -> Tüm karakterler sayi ise True, değilse False.
string.isalnum() -> Harf veya rakam (alfanümerik) ise True, değilse False.
string.islower() -> Tüm harfler küçük ise True, değilse False.
string.isupper() -> Tüm harfler büyük ise True, değilse False.
"""
"""cumle=input("lutfen istediginiz cumleyi yaziniz:")
cumle=cumle.upper() #buyuk harfe cevirdik

#simdi split fonksiyonu kelimeleri ayirip listeye ceviriyoruz
kelimeler=cumle.split()
#kelimeleri ters cevir
kelimeler.reverse()
#tekrar birlestirme islemi
yeni_cumle=" ".join(kelimeler) #string ifade istiyorum
print("donusturulmus cumle:", yeni_cumle)"""

#kelime ters cevirme cozum 1
kelime=input("lutfen istediginiz kelimeyi giriniz:")
print("kelimeniz:",kelime)
kelime_list=list(kelime)
kelime_list.reverse()
ters_cevirilmis_hali= "".join(kelime_list)
print("ters cevirilmis kelimeniz:",ters_cevirilmis_hali)

#ters cevirme cozum 2
kelime=input("lutfen istediginiz kelimeyi giriniz:")
ters_kelime=" "
for harf in kelime:
    ters_kelime=harf+ters_kelime
print("ters cevirilmis hali:",ters_kelime)   
