#sayi tahmim oyunu
import random
def sayi_tahmini():
    
    sayi=random.randint(1,100)
    tahmin_hakki=7

    while tahmin_hakki>0:
        tahmin_girdisi=input("lutfen sayi giriniz:")
        if not tahmin_girdisi.isdigit(): #sayi mi degil mi kontrolu
            print("lutfen gecerli bi deger giriniz:")
            continue
           
        tahmin=int(tahmin_girdisi)
        if tahmin==sayi:
            print("tebrikler! bildiniz")
            break
        elif tahmin<sayi:
            print("girdiginiz sayi küçük lutfen arttirin")
            tahmin_hakki=tahmin_hakki-1
            print("kalan hakkiniz:",tahmin_hakki)
        elif tahmin>sayi:
            print("girdiginiz sayi buyuk azaltin")
            tahmin_hakki=tahmin_hakki-1
            print("kalan hakkiniz:",tahmin_hakki)
    if tahmin_hakki==0:
        print("tahmim hakkiniz bitti asil sayi:",sayi)
#Ana Program Döngüsü
# oyuncu "Evet" dediği sürece oyunun sonsuza kadar tekrar oynanabilmesini sağlar.      
while True:
    sayi_tahmini()
    tekrar_oynamak=input("tekrar oynamak ister misiniz(E/H):")
    # .lower() ile kullanıcının girdiği harfi küçük harfe dönüştürüyoruz (E -> e).
    # '!=' ifadesi 'Eşit Değilse' demektir. Yani yanıt 'e' (Evet) DEĞİLSE bu blok çalışır.
    if tekrar_oynamak.lower()!="e":
        print("oyun bitti gorusmek uzere")
        break