sayi=float(input("lutfen bir sayi giriniz: "))
if sayi>20 and sayi%2!=0:
    print("girdiginiz sayi 20 den buyuk ve tek bir sayidir.")
else:
    print("girdiginiz sayi kriterleri karsilamiyor.")
    
#IN kullanimi
mevcut_meyveler=["elma","armut","muz","kiraz"]
girilen_meyve=input("lutfen bir meyve giriniz: ")
if girilen_meyve in mevcut_meyveler:
    print(" meyveler listesinde var.")
else:
    print(" meyveler listesinde yok.")  #in kullanimi ile bir elemanin listede olup olmadigini kontrol edebiliriz.

#slicing kullanimi
sehirler=["ankara","istanbul","izmir","antalya","adana","trabzon","bursa"]
print(sehirler[2:5])  # 2 dahil 5 haric olmak uzere 2. indexten 5. indexe kadar olan elemanlari yazdirir.
print(sehirler[:4])  # 0. indexten 4. indexe kadar olan elemanlari yazdirir.
print(sehirler[3:])  # 3. indexten son indexe kadar olan elemanlari yazdirir.
print(sehirler[1:6:2])  # 1. indexten 6. indexe kadar olan elemanlari 2'ser atlayarak yazdirir.
#1. nin output izlenimi: ['izmir', 'antalya', 'adana']
#2. nin output izlenimi: ['ankara', 'istanbul', 'izmir', 'antalya']
#3. nin output izlenimi: ['antalya', 'adana', 'trabzon', 'bursa']
#4. nin output izlenimi: ['istanbul', 'antalya', 'trabzon']
""" listeler disinda stringlerde de slicing kullanabiliriz. """


