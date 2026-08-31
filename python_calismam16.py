"""class Tesla1:
    sis_fari=2  #bu degistirilemez ne girdiysek o
    tesla_count=0
#yani bu class degiskeni. degistirebildiklerimiz nesne degiskenleri
    def __init__(self,rengi="beyaz",bataryasi="uzun menzil",janti=21,otopilot=True):
        self.renk=rengi
        self.batarya=bataryasi  #self hep olmak zorunda
        self.jant=janti     #nesne degiskenleri
        self.otopilot=otopilot
        Tesla1.tesla_count+=1 #her cagirisimizda artsin

    def goster_bilgi(self):
        print(f"renk:{self.renk},batarya:{self.batarya},jant:{self.jant},"
        f"otopilot:{self.otopilot}")
   
        
benim_teslam=Tesla1() #object
benim_teslam.goster_bilgi()
aysenin_teslasi=Tesla1()
aysenin_teslasi.goster_bilgi()

print("sis fari sayisi:",Tesla1.sis_fari) #sınıf
print("benim teslamin rengi",benim_teslam.renk) #nesneyi yazarken böyle, cunku tum arabalar 
#beyaz olmak zorunda degil ama iki tane farı olmak zorunda gibi dusun.abs
benim_teslam.sis_fari=3
print("benim arabamin sis fari sayisi:",benim_teslam.sis_fari) #3
print("sis fari sayisi:",Tesla1.sis_fari)#2
#neden? cunku benım teslam ıcın degistirdik genelde bi degisim yapmadik
#yani benim teslam için o satirlik nesne degiskeni gibi davrandi
benim_teslam.sun_roof=True
print("benim teslamda sunroof:",benim_teslam.sun_roof)
#print("aysenin teslasinda sunroof:",aysenin_teslasi.sun_roof) yazarsam olmaz cunku sadece o satir icin tanimladik
#olmasini istiyorsam bu satir icinde tanimlicaktim. yani yine genelde bi degisim yapmadim!
print("toplam tesla sayisi:",Tesla1.tesla_count)
"""
#oop prensipleri ENCAPSULATION PRENSIBI
class Tesla1:
    sis_fari=2  
    tesla_count=0
    GECERLI_RENKLER=["beyaz","siyah","kirmizi"]

    def __init__(self,rengi="beyaz",bataryasi="uzun menzil",janti=21,otopilot=True):
        #eger verilen renk gecerli degilse varsaiyaln renk beyaz ayarlanir
        if rengi in Tesla1.GECERLI_RENKLER:
            self.__renk=rengi #Normalde self.renk yazsaydık, dışarıdan isteyen herkes araba.renk = "pembe" diyerek rengi değiştirebilirdi.
        else:
            self.__renk="beyaz"
        
        self.batarya=bataryasi  
        self.jant=janti     
        self.otopilot=otopilot
        Tesla1.tesla_count+=1 

    def goster_bilgi(self):
        print(f"renk:{self.__renk},batarya:{self.batarya},jant:{self.jant},"
        f"otopilot:{self.otopilot}")
    def set_renk(self,yeni_renk): # Gizli olan __renk değişkenini sadece izin verilen kurallarla güncellemeye yarar.
        #fnksiyonı burada bir Güvenlik Görevlisi (Kontrol Noktası) görevi görür.
        if yeni_renk in Tesla1.GECERLI_RENKLER:  #Sadece izin verilen renkler ("beyaz","siyah","kirmizi") girilirse onay verir.
            self.__renk=yeni_renk
        else:
            print("gecersiz renk", yeni_renk)
    def get_renk(self):
        return self.__renk   #bunun sayesinde parametlerden sadec rengi vericek
   
 # 1. 'turuncu' geçersiz renk olduğu için __init__ içindeki if-else 'turuncu'yu reddeder.
# Araba otomatik olarak varsayılan 'beyaz' rengiyle üretilir.       
benim_teslam=Tesla1(janti=21,rengi="turuncu") 

#
# set_renk fonksiyonu çalışır. 'turuncu' GECERLI_RENKLER listesinde olmadığı için
# ekrana "gecersiz renk turuncu" uyarısı basılır ve arabanın rengi 'beyaz' kalmaya devam eder.
benim_teslam.set_renk("turuncu")
print("benim teslam:")
benim_teslam.goster_bilgi()

aysenin_teslasi=Tesla1()  # Parametre verilmediği için tüm varsayılan değerlerle (beyaz renk) üretilir.
# 'kirmizi' geçerli listede olduğu için set_renk güvenlik duvarını geçer.
# self.__renk değeri başarılı bir şekilde 'kirmizi' olarak güncellenir.
aysenin_teslasi.set_renk("kirmizi")
print("aysenin teslasi:")
aysenin_teslasi.goster_bilgi()

ahmetin_teslasi=Tesla1(janti=21,rengi="siyah")
print("ahmetin teslasinin rengi",ahmetin_teslasi.get_renk())



