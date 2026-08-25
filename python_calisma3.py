
#PRATIK
sayi1=float(input("Birinci sayiyigiriniz: "))
sayi2=float(input("Ikinci sayiyi giriniz: "))
sayi3=float(input("Ucuncu sayiyi giriniz: "))
ortalama=(sayi1+sayi2+sayi3)/3
yuvarlanmis_ortalama=round(ortalama,1) #round() fonksiyonu ile ortalama değerini 1 basamaklı yuvarla
print("ortalama sonucu:", yuvarlanmis_ortalama)
print(f"ortalama sonucu: {yuvarlanmis_ortalama}") #f-string ile ortalama değerini yazdırır
#
# MODUL KULLANIMI
import math #math modülünü import ettik.
print(math.sqrt(16)) # *output=4.0 , math modülündeki sqrt() fonksiyonu ile 16'nın karekökünü aldık.
print(math.floor(3.9)) # *output=3 , math modülündeki floor() fonksiyonu ile 3.9'un alt tam sayısını aldık.
print(math.ceil(3.1)) # *output=4 , math modülündeki ceil() fonksiyonu ile 3.1'in üst tam sayısını aldık.
print(math.pow(2,3)) # *output=8.0 , math modülündeki pow() fonksiyonu ile 2'nin 3. kuvvetini aldık.
print(math.log(100,10)) # *output=2.0 , math modülündeki log() fonksiyonu ile 100'ün 10 tabanındaki logaritmasını aldık.
print(math.log(100)) #ln100 , math modülündeki log() fonksiyonu ile 100'ün doğal logaritmasını aldık.  
print(math.log10(100)) # *output=2.0 , math modülündeki log10() fonksiyonu ile 100'ün 10 tabanındaki logaritmasını aldık.
""" from math import sqrt, floor, ceil, pow, log, log10
 math modülünden sadece gerekli fonksiyonlari import ettik. 
  yani math.sqrt() yerine direkt sqrt() fonksiyonunu kullanabiliriz."""
