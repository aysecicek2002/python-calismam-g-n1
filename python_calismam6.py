#FOR DONGUSU
"""yaslar=[12,15,18,20,25,30]
for yas in yaslar: #burada yas degiskeni yaslar listesindeki her bir elemani tek tek alir ve dongu icinde kullanir.
    print(yas)
#yani eksradan yas diye bir degisken tanimlamaya gerek yok. for dongusu bunu kendisi yapar.


# range() fonksiyonu ile de for dongusu kullanabiliriz.
for i in range(5): #range() fonksiyonu 0 dan baslayarak 5 e kadar olan sayilari tek tek alir ve dongu icinde kullanir.
    print(i) 
for i in range(1,10): #range() fonksiyonu 1 den baslayarak 10 a kadar olan sayilari tek tek alir ve dongu icinde kullanir.
    print(i)       
for i in range(1,10,2): #range() fonksiyonu 1 den baslayarak 10 a kadar olan sayilari 2'ser atlayarak alir ve dongu icinde kullanir.
    print(i)

#range fonksiyonu kullanarak otomatik olarak bir liste olusturabiliriz.
sayilar=list(range(1,10)) #range() fonksiyonu 1 den baslayarak 10 a kadar olan sayilari tek tek alir ve listeye atar.
print(sayilar)  
for i in range(10,19,-1): #range() fonksiyonu 10 dan baslayarak 19 a kadar olan sayilari 1'er azalarak alir ve dongu icinde kullanir.
    print(i)"""
"""
# 1 den 100 e kadar(1 ve 100 dahil) tüm sayıların toplamını hesaplayan bir program yazınız.
toplam=0
for i in range(1,101):
    toplam+=i       
    
print("1 den 100 e kadar olan sayilarin toplami: ",toplam)"""

"""
#odev tek sayilar toplami
baslangic_sayisi=int(input("lutfen baslangic sayisini giriniz: "))
bitis_sayisi=int(input("lutfen bitis sayisini giriniz:")) # 
toplam=0
for sayi in range(baslangic_sayisi,bitis_sayisi+1): #bitis sayisini dahil etmek icin +1 ekledik
    if sayi%2!=0: # sayi tek mi kontrol edildi 
        print("tek sayilar: ",sayi)
        toplam+=sayi # if blokunda toplama ekleme islemi yapildi. sadece tek sayilar toplandi.
   
    
print("tek sayilarin toplami: ",toplam) #döngü sonunda yazdık tek seferde tüm toplami görmek için"""

"""

#1 den 10 a kadR olan sayıların karesini alma
karesi=[ ]
for sayi in range(1,11):
    karesi.append(sayi**2) #sayilarin karesini ekledik 
print("sayinin karesi:", karesi)   

#ya da
karesi=[sayi**2 for sayi in range(1,11)] #iki kodun da sonucu aynı olur.
print(karesi) """

"""sayilar=[1,2,3,4,5,6,7,8,9,10]
cift_sayilar=[]
for i in sayilar:
    if i%2==0:
        cift_sayilar.append(i) #cift sayilari listeye ekledik
print("cift sayilar bunlardir: ",cift_sayilar)     """   

#ya da
"""
sayilar=[1,2,3,4,5,6,7,8,9,10]
cift_sayilar=[i for i in sayilar if i%2==0]
print(cift_sayilar)
cift_sayilarin_karesi=[i**2 for i in sayilar if i%2==0]
print(cift_sayilarin_karesi) """
#
"""kelimeler=["ayse","fatma","gokdeniz","kitap"]
buyuk_harf=[kelime.upper() for kelime in kelimeler]
print(buyuk_harf)
#ya da
buyuk_harf=[]
for kelime in kelimeler:
    buyuk_harf.append(kelime.upper())
print(buyuk_harf)"""


