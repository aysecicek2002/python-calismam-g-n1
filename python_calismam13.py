#parametre verilmezse varsayilan degeri kullanmak (tuple olarak alır)
"""def selamla(isim="misafir kullanici"): #sonradan cagirdigimiz fonksiyona bir sey atamazsak kullanilir icindeki deger
    print("merhaba", isim)
selamla("ahmet")
selamla()  """

"""#belirsiz sayida parametre *args
def topla(*sayilar): #istedigimiz kadar deger yazabiliriz basina* koyarak
    return sum(sayilar) #degrleri topladik
print(topla(1,2,45,67,4,54))"""

"""
def agirlikli_ortalama_hesapla():
    vize1=int(input("lutfen 1. vize notunuzu giriniz:"))
    vize2=int(input("lutfen 2. vize notunuzu giriniz:"))
    final=int(input("lutfen final notunuzu giriniz:"))
    print("notlariniz sirasiyla:",vize1,vize2,final,"budur.")
    hesap=((vize1*20/100)+(vize2*35/100) +(final*45/100))
    print("agirlikli ortalamaniz:",hesap)
    if hesap<50 or final<20:
        print("maalesef butunlemeye kaldiniz")
agirlikli_ortalama_hesapla() """
#######################################3


#kwags kullanimi
# **kwargs, isimli parametreleri bir sözlük (dict) olarak alır. fex:**isimler,**notlar vs 
# Bu sayede dinamik ve esnek fonksiyonlar yazabiliriz.
# İçindeki anahtar (key) ve değer (value) çiftlerini kullanabiliriz.
"""
def kisi_bilgileri(**kwargs):
    print(kwargs)

kisi_bilgileri(ad="Ahmet", yas=25, sehir="Ankara")  #output->{'ad': 'Ahmet', 'yas': 25, 'sehir': 'Ankara'}

def kisi_bilgileri1(**bilgiler):
    for key,value in bilgiler.items():
        print(f"{key}: {value}")
  
kisi_bilgileri(ad="Ahmet", yas=25, sehir="Ankara")

"""

"""
def kisi_bilgileri1(**bilgiler):
   
    print("yas:",bilgiler["yas"])  #sadece yas parametresini alir
  
kisi_bilgileri1(ad="Ahmet", yas=25, sehir="Ankara")
 """

#lambda (anonim) fonksiyonlar-> kucuk ve tek satırlık islemler icerisinde kullanilirlar
topla= lambda x, y: x+y
print(topla(3,5)) #   output=8
print((lambda x,y: x+y)(3,5)) #output=8

kupu=lambda u,z: u**z
print(kupu(3,4))    #81
print((lambda u,z:u**z)(3,4)) #81

#recursive fonksiyonlar (ozyinelemeli) ->fonksiyonun kendi kendini cagirmasina özyineleme denir.
def faktoriyel(n):
    if n==1:  #n=1 oldugunda dur 1!=1 degeri olur ve bekleyen diger faktöriyelleri yapar.
        return 1   #4!=4*3!  ,3!=3*2!  ,2!=2*1! burdan geriye dogru cozer 1!=1 di zaten (return 1 )
    return n*faktoriyel(n-1)
print(faktoriyel(4))  #24

#fonksiyonlari parametre olarak kullanmak-> fonksiyonlar baska fonksiyonlara parametre olarak verilebilir.
def ikiyle_carp(fonksiyon,sayi):
    return fonksiyon(sayi)*2  #fonksiyon olarak kare_al ;sayi olarak 4 aldık
def kare_al(x):
    return x**2
print(ikiyle_carp(kare_al,4))   
#fonksiyonlarin veri yapilarini parametre olrak almasi  ve dondurmesi
def liste_toplam(listem,isim):
    print("merhaba!",isim)
    return sum(listem)
sayilar=[10,20,30,40,50]
sonuc=liste_toplam(sayilar,"ali")
print("listelerinizin toplami:",sonuc)


#listedeki sayilardan çift olanlrla yeni liste
def cift_say_listesi(sayilar):
    return [x for x in sayilar if x%2==0]
sayi_listesi=[1,2,3,4,5,6,7,8]                 
sonuc=cift_say_listesi(sayi_listesi)
print(sonuc)

#icinde kar gecen kelimelrifiltrele
def kar_filtre(kelimeler):
    sonuc=[]
    for kelime in kelimeler: 
        if "kar" in kelime: #eger kar kelimesini iceriyorsa
            sonuc.append(kelime)
    return sonuc
kelimeler_listesi=["kardan adam","karpuz","kalem","karin","kaybolmak"]
print("kar filtreli listemiz:",kar_filtre(kelimeler_listesi))
        


def fib_serisi():
    n=int(input("lutfen 2 'den buyuk sayilari yaziniz:")) #burada n degerini girmemiz gerek
    if n<=2:
        print("HATA! lutfen 2 den buyuk sayi yazniz")
    fib_listesi=[]
    a=0
    b=1
    while a<=n:  #fex:28 girdik son eleman onndan buyuk olamaz
        fib_listesi.append(a)  #burda ilk elamanı yazdırdık fib de ilk eleman 0 sonra 1 sonra toplamları 1 vs...
        temp=a+b  #3. eleman a+b olur
        a=b #4. eleman için yenı a degeri b olur b degeri de temp olur fex: 0 1 1 2 3 burada 4. elaman icin 1+1 i topldik
        b=temp
    print("fibonacci sayşlarimiz:",fib_listesi)    
fib_serisi()


