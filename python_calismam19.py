#hata yonetimi
#hata yoneyimi icin try-except kod blogu kullanilir.
#ornegin kullanicdan bi sayi alip 10 a bolmesini isteyen bi program yazalim.0 a bolemıyoruz hata verdi napıcaz (zerodivisionerror)
"""while True:
    try:    #hata olabilecek yeri yaziyoruz
        sayi=int(input("lutfen bir sayi giriniz:"))
        bolme_sonucu=10/sayi
        print("bolme sonucunuz:",bolme_sonucu)
     
    except ZeroDivisionError: #hatayi yakalayan kisim
        print("HATA! bir sayi 0 a bolunemez")
    #program cokmez kaldıgi yerden devam eder
    except ValueError:#sayi disinda bir sey girersek
        print("HATA! girdiginiz bir sayi degil")
    
#ben ekstradan while dongusunde surekli donguye aldım surekli sorup girmek ıcın
print("selam")

#except exception as e:
#   print(f"bir hata olustu {e})  -->burda hata turunu bılmıyorsak hepsini kapsayan exceptiondan yaparız {e} hata turunu gosterir

"""
"""
try:
    liste=[17,16,15]
    index=int(input("lutfen bi sayi giriniz:"))
    print("secilen eleman:",liste[index])

except IndexError:
    print("hata secilen index liste eleman sinirini asti")
else:
    print("kodunuz hatasizdir tebrikler") #sadece sorunsuz hatasiz oldugunda calisir
finally: #hata olsa da olmasa da son mesaji vermek için yazilir
    print("islem tamamlandi")


print("selam....") """


#RAISE ILE KENDI HATAMIZI FIRLATMA
#bilerek hatali yapiyorum lısteyi
liste=[10,"x",3,"y",5]
gecerli_sayilar={1,2,3,4,5,6,7,8,9,10}
  
for i in liste:
    try:
        if i not in gecerli_sayilar:
            raise ValueError(f"hata! {i} gecerli degil")
    except ValueError as e:
        print("hata yakalandi:",e)
        continue
    print("sayilarin karesi:",i**2)