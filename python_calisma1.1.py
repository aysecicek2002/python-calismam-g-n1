#pythonda print komutu icinde "" ya da '' islevi aynidir
print("hello world")
print('hello world')  
#cls terminal kisima yazinca temizler


#print kullanimi
''' pythonda hatali islemden sonrasi yazilmaz. hata sonrasi dogru 
olsa bile python okumaz bunu. bunun sebebi INTERPRETED dil olmasindan 
kaynaklidir. syntax hatalarinda direkt kod calismaz!!!!
''' 
print(""" hello world
selam dunya
ben ayse""") #bu sekilde tek printle bircok sey yazabiliriz
###########
#ILK ODEV-> tek print içinde birden cok satırlı yaz
print(""" python programlama:
\t\t-kolay
\t\t-eglenceli
\t\t-guclu""" )  


###########
'''
\t : bir tab bosluk
\n : yeni satira geçer
->kesme işaretini print icinde kullanmqk icin " \ " gerekli
'''
print(' ahmet\'in kitabi') 
#########

#ODEV2-> aynısını \t \n yardımıyla yap
print("\tpython programlama:\n\t-kolay\n\t-eglenceli\n\t-guclu")
#########

print("merhaba\t" + input("lutfen adinizi giriniz:")+"  hosgeldin!" )
#->burada input a istedigimiz seyi atiyoruz ve print icine onu yaziyor

#DEGISKENLER
isim = input("lutfen adinizi giriniz: ")
print("merhaba\t"+ isim +" hosgeldiniz")
print("yapmak istedigin islemi secer misin? " + isim)
'''
burada ise inputu degisken kullanarak sakladik
 ve bir soonraki islemler icin de atama yardimiyla
her defasinda sorma islemini tekrarlamadan kullandik
** tabi burada kendimiz de değer atayarak yapabilirdik. bu ornek 
kullaniciya sorma kalibi.
'''
