"""
#KOSULLU İFADELER
sicaklik_degeri= float(input("lutfen sicaklik degerinizi yaziniz: ")) #sadece input yaparsak type hatasi aliriz. bu yuzden float ile ceviriyoruz.
print("sicaklik degeriniz: ", sicaklik_degeri," derece")
if sicaklik_degeri > 37:
    print("sicaklik degeriniz normalin ustunde,")
    print("sagliginizi kontrol ettiriniz. lutfen doktorunuza basvurunuz.")
else:
    print("sicaklik degeriniz normal sinirlardadir.") """
       
"""sayi=float(input("lutfen bir sayi giriniz: "))
if sayi>0:
    print("girdiginiz sayi pozitif bir sayidir.")   
elif sayi==0:
    print("girdiginiz sayi sifirdir.")
else:
    print("girdiginiz sayi negatiftir.")"""


#yasa göre ates derecesi kontrolü kodum
yasiniz=int(input("lutfen yasinizi giriniz: "))
if yasiniz<=18:
    print("yasiniz 18 den kucuk")
    ates_derecesi=float(input("lutfen ates derecenizi giriniz: "))
    if ates_derecesi<=37.2:
        print("ates dereceniz normal sinirlardadir.")
    elif 37.2<ates_derecesi<=38:
        print(" kritik sinir. lutfen dikkatli olunuz.")
    elif 38<ates_derecesi<=39:
        print(" ates dereceniz cok yuksek. lutfen hemen bir sağlik kuruluşuna gidiniz.")
    else:
        print("cocuklarda kalici saglik sorunlari yaratabilir. lutfen hemen bir sağlik kuruluşuna gidiniz.")
else:
    print("yasiniz 18 den buyuk")
    ates_derecesi=float(input("lutfen ates derecenizi giriniz: "))
    if ates_derecesi<=37:
        print("ates dereceniz normal sinirlardadir.")
    elif 37<ates_derecesi<=38:
        print("ates dereceniz biraz yuksek.")  
    elif 38<ates_derecesi<=39:    
        print("ates dereceniz cok yuksek.saglik kuruluşuna basvurunuz.")
    else:
        print("acil saglik sorunlari yaratabilir. lutfen hemen bir sağlik kuruluşuna gidiniz.")
print("sagliginiza lutfen dikkat ediniz. saglikli gunler dileriz.")        