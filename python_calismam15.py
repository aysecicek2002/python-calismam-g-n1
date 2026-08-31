#OOP
"""
class tesla:
    renk="mavi"  #class
    batarya="uzun menzil"
    jant=20
    otopilot= False
benim_teslam=tesla() #object
print(benim_teslam.renk,benim_teslam.batarya,benim_teslam.jant,benim_teslam.otopilot)
benim_teslam.jant=21  #yanı degistirilebilir
print(benim_teslam.renk,benim_teslam.batarya,benim_teslam.jant,benim_teslam.otopilot)
#tek bi classtan bircok object olusturabilirz."""
"""
#initializer method ve self kullanimi
#initalizer
class tesla1:
    def __init__(self,rengi="beyaz",bataryasi="uzun menzil",janti=21,otopilot=True):
        self.renk=rengi
        self.batarya=bataryasi  #self hep olmak zorunda
        self.jant=janti
        self.otopilot=otopilot

    def goster_bilgi(self):
        print(f"renk:{self.renk},batarya:{self.batarya},jant:{self.jant},otopilot:{self.otopilot}")


benim_teslam=tesla1() #object
benim_teslam.goster_bilgi()
# Varsayılanlar yerine özel seçimler yapıyoruz:
arkadasimin_teslasi = tesla1(rengi="kirmizi", janti=19, otopilot=False)
arkadasimin_teslasi.goster_bilgi()
# Çıktı: renk:kırmızı,batarya:uzun menzil,jant:19,otopilot:False """


class tesla1:
    def __init__(self,rengi="beyaz",bataryasi="uzun menzil",janti=21,otopilot=True):
        self.renk=rengi
        self.batarya=bataryasi  #self hep olmak zorunda
        self.jant=janti     #nesne degiskenleri
        self.otopilot=otopilot
        self.hiz=0

    def goster_bilgi(self):
        print(f"renk:{self.renk},batarya:{self.batarya},jant:{self.jant},"
        f"otopilot:{self.otopilot},hiz{self.hiz}")
    def hizlan(self,miktar):
        self.hiz+=miktar
    def yavasla(self,miktar):  #bircok fonksiyon ekleyebiliriz
        self.hiz-=miktar
        
benim_teslam=tesla1() #object
benim_teslam.goster_bilgi()
aysenin_teslasi=tesla1(rengi="mor",janti=19)
aysenin_teslasi.hizlan(30)
aysenin_teslasi.yavasla(50)
aysenin_teslasi.hizlan(70)
aysenin_teslasi.goster_bilgi() #renk:mor,batarya:uzun menzil,jant:19,otopilot:True,hiz50