#WHILE DONGUSU
"""
programda donguler belirli bir islemi belirli bi kosul sagladigi sürece donmeye devam
eder. 
while dongusu kosul true oldugu surece devam eder.kosul false olursa dongu biter.
hangi durumlarda whilw dongusunu tercih etmeliyiz?
-dongu sayisi belli degilse veya kosula bagli tekrar eden islemler icin.
"""
"""
x=0
while x<10:
    print(x)
    x+=1 #for dongusunden farkli olarak her dongu sonunda sayiyi arttirmamiz lazim
    #eger arttirmazsak dongude surekli sifir doner.

x=0
toplam=0
while x<100:
    toplam+=x
    x+=1
print(toplam) #dongu satirinda yaparsam her yapılan toplam islemini yazar
#ama dongu sonunda yazarsam direkt 100 e kadar olan tum sayilarin toplamini yapar.

#peki for ve while dongusu farklari nelerdr

sum1=0
for x in range(0,100):
    sum1+=x
print(sum1)
#whiledan farkli olarak x i her dongu sonunda arttirmak icin bi islem yapmadik.
#for dongusu zaten bunu keni yapiyor.


while True:
    sayi=float(input("lutfen istediginiz sayiyi giriniz: "))
    if sayi<0:
        print("negatif sayi girdiniz programda cikiliyor")
        break
    else:
        sayinin_karesi=sayi**2
        print("girdiginiz sayinin karesi:",sayinin_karesi) """

#hesap makinesi
while True:
    
    
    print("""toplama=1
             cikarma=2
             bolme=3
             carpma=4
             mod_alma=5
             cikis=6""")

    sonuc=0
    sayi1=float(input("lutfen istediginiz sayiyi giriniz: "))
    sayi2=float(input("lutfen istediginiz 2. sayiyi giriniz: "))
    yapilacak_islem=int(input("lutfen yapacaginiz islemi seciniz(1-6): "))
    if yapilacak_islem==1:
        sonuc=sayi1+sayi2
        print("toplama isleminizin sonucu:",sonuc)
    elif yapilacak_islem==2:
        sonuc=sayi1-sayi2
        print("cikarma isleminizin sonucu:",sonuc)
    elif yapilacak_islem==3:
        sonuc=sayi1/sayi2
        print("bolme isleminizin sonucu:",sonuc)
    elif yapilacak_islem==4:
        sonuc=sayi1*sayi2
        print("carpma isleminizin sonucu:",sonuc)
    elif yapilacak_islem==5:
        sonuc=sayi1%sayi2
        print("mod alma isleminizin sonucu:",sonuc)
    elif yapilacak_islem==6:
        print("cikis yapildi")
        break




    
