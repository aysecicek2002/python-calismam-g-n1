"""cumle=input("lutfen istediginiz cumleyi giriniz:")
harf=input("lutfen istediginiz harfi giriniz:")
cumle_tup=tuple(cumle)
print("sectiginiz harf:",harf,"tekrar etme sikligi:",cumle_tup.count(harf))"""


"""
#1 ilw 35 arasinda 7 adet tam sayidan olusan listeyi uret
import random
sicaklik_degerleri=[] #ici bos liste olusturduk
for i in range(7):#haftanin günleri fex:0->pazartesi 6->pazar
    random_sicaklik= random.randint(1,35)
    sicaklik_degerleri.append(random_sicaklik) #bos listeye ekledik
print("random sicaklik degerleri:",sicaklik_degerleri )  #yazdirdik
ortalama_sicaklik=sum(sicaklik_degerleri)/7
print("ortalama sicaklik:",round(ortalama_sicaklik,2)) #virgulden sonra 2 bas. yazdirdik
"""
"""
number_list=[1,1,2,3,4,5,5,5,6,7,8,9]
number_set=set(number_list)
print(number_set)
number_list=list(number_set)
print(number_list)


kitaplar=[("seker portakali",98),   #list ve tuple iç içe
      ("icimizdeki seytaan",50),
      ("kurk mantolu madonna",120),
      ("1984",22)
]
for kitap in kitaplar:
    print(kitap[0],kitap[1]) 

for kitap,sayfa_sayisi in kitaplar:
    print(kitap,sayfa_sayisi)
"""
################### sinav notu yazdirma
ogrenciler={
101:[96,35,80],
102:[100,78,90],
103:[98,89,90]
}

for okul_no,sinav_notlari in ogrenciler.items():
    print(f"okul numarasi: {okul_no}")
    for notlari in sinav_notlari:
        print(f"notu: {notlari}")
    print()


############################
    kitaplar=[("seker portakali",200),   #list ve tuple iç içe
      ("icimizdeki seytaan",150),
      ("kurk mantolu madonna",120),
      ("1984",171)
]
total_sayfa_sayisi=0
for kitap_adi,kitap_sayfasi in kitaplar:
    print(kitap_adi,":",kitap_sayfasi)
    if kitap_sayfasi>170:
        print("sayfa sayisi 170 den buyuk")
        total_sayfa_sayisi+=kitap_sayfasi
    else:
        print("sayfa sayisi 170 den kucuk")
print("total sayfa sayisi:",total_sayfa_sayisi)