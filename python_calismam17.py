#INHERITANCE(KALITIM)
"""class Hayvan:
    def __init__(self,isim,yas):
        self.isim=isim
        self.yas=yas
    def ses_cikarma(self):
        print("hayvan ses cikarir")   
    def kosma(self):
        print("hayvan kosar")
class Kedi(Hayvan): #hayvan sinifindan miras aldi
    def __init__(self,isim,yas,renk):#diger hayvana ozgu parametreleri kaybetmeden yenisini ekleme
        super().__init__(isim,yas)# ata koddan alıyoruz isim ve yas ı
        self.renk=renk #kedilere ozel renk ozelliği actık
       

    def tirmanma(self):
        print(f"{self.isim} tirmanir")
        #override uzerine yazmak
    def ses_cikarma(self):
        print(f"{self.isim} miyavvv lar")
class Kopek(Hayvan):
    def guclu_cene(self):
        print(f"{self.isim}  guclu cene yapisina sahiptir")

kedi1= Kedi("minnos",2,"beyaz")
kopek1= Kopek("karabas",1)
kedi1.ses_cikarma() #normalde output hayvan ses cikarir override kullanarak ozellestirdigimizde is farklı
kopek1.ses_cikarma() #hayvan ses cikarir
kedi1.tirmanma()
kopek1.guclu_cene()
print("kedinizin rengi:",kedi1.renk)"""

#POLYMORPHIZM(COK BICIMLILIK)
"""
class Hayvan:
    def __init__(self,isim,yas):
        self.isim=isim
        self.yas=yas
    def ses_cikarma(self):
        print("hayvan ses cikarir")   
    def kosma(self):
        print("hayvan kosar")
class Kedi(Hayvan): 
    def __init__(self,isim,yas,renk):
        super().__init__(isim,yas)
        self.renk=renk 
       

    def tirmanma(self):
        print(f"{self.isim} tirmanir")
        #override uzerine yazmak
    def ses_cikarma(self):
        print(f"{self.isim} miyavvv lar")
class Kopek(Hayvan):
    def ses_cikarma(self):
        print(f"{self.isim} havv lar")
    def guclu_cene(self):
        print(f"{self.isim}  guclu cene yapisina sahiptir")
def hayvan_konustur(hayvan):
    hayvan.ses_cikarma() #***

kedi1= Kedi("minnos",2,"beyaz")
kopek1= Kopek("karabas",1)
hayvan_konustur(kedi1)

"""
#ABSTRACTION(SOYUTLAMA)
#karmasik sistemlerin ic detaylarini gizleyip,sadece disariya acilmasi gereken onemli fonk. sunar
from abc import ABC, abstractmethod #kullabilmek icin once bunu tanimla
#soyut sinif olustur
class Sekil(ABC):
    @abstractmethod # @abstractmethod dekoratörü: "Bu bir soyut metottur" anlamına gelir.
    def alan_hesapla(self):
        pass #islem yapilmicaksa bile yazilir
#Gövdesini boş bırakıyoruz (pass), çünkü "Sekil" tek başına soyut bir kavramdır (kare mi, daire mi belli değil).
#Şeklin ne olduğu belli olmadığı için alanının nasıl hesaplanacağı da burada bilinemez.
    
    #alt siniflar bunu override etmeli
    #alt sinif yap

class Kare(Sekil): #Kare sınıfı (Sekil) soyut sınıfını miras alıyor (Inheritance).
    def __init__(self,kenar):
        self.kenar=kenar
# ZORUNLU KURALIN YERİNE GETİRİLMESİ (OVERRIDE):
# Sekil sınıfı bize "alan_hesapla zorunlu" demişti.
    def alan_hesapla(self):
        return self.kenar**2
class Daire(Sekil):
    def __init__(self,yari_cap):
        self.yari_cap=yari_cap
    def alan_hesapla(self):
        return 3.14 * (self.yari_cap)**2

def seklin_alanini_yaz(Sekil):
    print(f"seklin alani {Sekil.alan_hesapla()}")

kare1=Kare(4) #kenarı belirledik
daire1=Daire(3)
seklin_alanini_yaz(kare1) #yazdirdik
seklin_alanini_yaz(daire1)