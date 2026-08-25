print(len("kaan")) #içeride yazan metnin uzunluğunu yazar *output=4
print(len("selam ben ayse")) #içeride yazan metnin uzunluğunu yazar *output=14
print(type("kaan")) #içeride yazanın türünü belirtir. *output=<class 'str'>
print(type(1.3)) # *output=<class 'float'>

# STRING VERI TIPI
isim= "ayse"
print(type(isim)) # *output=<class 'str'>
#
isim2="ayse"*4 + " "+"cicek"*4
print(isim2) #*output=ayseayseayseayse cicekcicekcicekcicek

girilen_kelime="aysenur"
print(girilen_kelime[0]) # *output=a, pythonda string veri tipinde indexleme 0'dan başlar.
print(girilen_kelime[6]) # *output=r, -6 ile 1 aynıdır. -1 ile 6 aynıdır.
# -2 ile 5 aynıdır. -3 ile 4 aynıdır. -4 ile 3 aynıdır. -5 ile 2 aynıdır. -6 ile 1 aynıdır.
""" A Y S E N U R
    0 1 2 3 4 5 6 --> DIREK INDEXLEME YAPILIRKEN KULLANILIR.
    0-6-5-4-3-2-1 -->TERS INDEXLEME YAPILIRKEN KULLANILIR.
"""
print(girilen_kelime[2:5]) # *output=sen , 2 dahil 5 dahil değil. 2,3,4 indexleri yazılır.
print(girilen_kelime[2:]) # *output=senur , 2 dahil 6 dahil değil. 2,3,4,5,6 indexleri yazılır.
print(girilen_kelime[:5]) # *output=aysen , 0 dahil 5 dahil değil. 0,1,2,3,4 indexleri yazılır.
print(girilen_kelime[1:2:3]) # *output=y , 1 dahil 2 dahil değil. 1 indexi yazılır. 3 atlayarak gider.
print(girilen_kelime[::2]) #*output=asnr , 0 dahil 6 dahil değil. 0,2,4,6 indexleri yazılır. 2 atlayarak gider.
#
print(girilen_kelime.upper()) # *output=AYSENUR , tüm harfleri büyük yapar.
print(girilen_kelime.lower()) # *output=aysenur , tüm harfleri küçük yapar.
print(girilen_kelime.replace("a","e")) # *output=eysenur , a harfini e harfi ile değiştirir.

print(girilen_kelime.split("e", maxsplit=1)) # *output=['ays', 'nur'] , e harfinden itibaren kelimeyi ikiye böler. maxsplit=1 ile sadece 1 kere böler.



#
#INT VERI TIPI
sayi=234567898765432234567 #diğer dillerden farklı olarak int veri tipi çok büyük sayıları da tutabilir.
print(sayi*3) #*output=703703696295296702401
#



#
#FLOAT VERI TIPI
ondalikli_sayi=3.14
print(type(ondalikli_sayi)) # *output=<class 'float'>
print(ondalikli_sayi) # *output=3.14
print(ondalikli_sayi*3) # *output=9.42
print(ondalikli_sayi+2.0) # *output=5.14
#



#BOOELAN VERI TIPI
mantiksal_deger=True
print(type(mantiksal_deger)) # *output=<class 'bool'>
print(10<12) # *output=True
print(10>12) # *output=False
print(not(10<1))# *output=True
print(10!=10) # *output=False cunku 10 eşit değildir 10'a demek istiyor. 10 eşittir 10 olduğu için False döner.
#pythonda dogru ve yanlıs değerleri True ve False olarak ifade eder. dieğer dillerde 1 ve 0 ile ifade edilir.
#


#LIST VERI TIPI
listem=[1,1.2,True,"kaan"] #->list veri tipi farklı veri tiplerini bir arada tutabilir.
print(type(listem)) # *output=<class 'list'>
listem=listem+[1,2,3] #listem listesine 1,2,3 elemanlarını ekler.
print(listem)# *output=[1, 1.2, True, 'kaan', 1, 2, 3]
#
listem.append("selam") #listeye selam elemanını ekler.
print(listem) # *output=[1, 1.2, True, 'kaan', 1, 2, 3, 'selam']
#
print(listem.pop()) # *output=selam , listeden son elemanı siler ve silinen elemanı döndürür.
print(listem) # *output=[1, 1.2, True, 'kaan', 1, 2, 3]
listem.pop() 
print(listem) # *output=[1, 1.2, True, 'kaan', 1, 2]
#
sayilarim=[1,22,3,4,5,62,7,86,9]
sayilarim.sort() #sayilarim listesini küçükten büyüğe sıralar.
print(sayilarim) # *output=[1, 2, 3, 4, 5, 7, 9, 22, 62, 86]
sayilarim.reverse() #sayilarim listesini ters çevirir.
print(sayilarim) # *output=[86, 62, 22, 9, 7, 5, 4, 3, 2, 1]
#
#TUPLE VERI TIPI
tuple1=(1,2,1,3,4,5,"a","b") #tuple veri tipi listeden farklı olarak değiştirilemez. yani tuple1[0]=10 gibi bir işlem yapılamaz.
print(tuple1.count(1)) # *output=2 , tuple1 içinde 1 elemanının kaç tane olduğunu sayar.
print(tuple1.index(3)) #output=3 , tuple1 içinde 3 elemanının indexini döndürür.   
#eğer tekrar eden eleman varsa ilk bulduğu indexi döndürür. ama olmayan bir eleman için index() fonksiyonu hata verir. 
#
#DICTIONARY VERI TIPI
dict1={"ad":"kaan",
"soyad":"cakmak",
"yas":20
} #dictionary veri tipi key-value (anahtar-değer) çiftlerinden oluşur.


dict2={"ad":"ayse",
"soyad":"cicek",
"yas":20,
"lokasyon": {
"dogum_yeri":"istanbul", 
"yasadigi_sehir":"ankara"
}
}
print(dict2)  #dictionaryde iç içe dictionary tanımlanabilir. 
print(dict2.get("yas")) # *output=20 , dict2 içindeki yas key'inin value'sunu döndürür. g
print(dict2.get("lokasyon").get("dogum_yeri")) # *output=istanbul , dict2 içindeki lokasyon key'inin value'su olan dictionary içindeki dogum_yeri key'inin value'sunu döndürür.
print(dic2.keys()) # *output=dict_keys(['ad', 'soyad', 'yas', 'lokasyon']) , dict2 içindeki key'leri döndürür.
print(dict2.values()) # *output=dict_values(['ayse', 'cicek', 20, {'dogum_yeri': 'istanbul', 'yasadigi_sehir': 'ankara'}]) , dict2 içindeki value'ları döndürür.    
