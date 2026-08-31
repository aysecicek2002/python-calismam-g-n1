# Bir iterator, üzerinde sırayla gezinilebilen (iterate edilebilen) bir nesnedir.

# Python'da iterator olan yapılar: list, tuple, set, dict, str gibi yapılardır.
# (for döngüsüyle erişebildiğimiz her şey iterabledır)

# - iter() fonksiyonu, bir iterable'dan bir iterator üretir.
# - next() fonksiyonu, sıradaki elemanı verir.
# - Eleman kalmadığında StopIteration hatası verir.
"""
meyveler=["elma","armut","kavun"]
it=iter(meyveler) #iterator urettik
meyve=next(it)
print(meyve) #bir daha cagirirsam armut u verir sonrasında kavun en sonunda hata verir """
"""
meyveler=["elma","armut","kavun"]
it=iter(meyveler) 
while True:
    try:
        meyve=next(it)
        print(meyve)
    except StopIteration: #burda hatayı yakaladık ve break attik
        break
print("bye")


#zip fonksiyonu-> 2 veya daha fazla listeyi eslestirir.

isimler=["ayse cicek","elanur sonmez","feriha yilmaz"]
notlar=[90,59,9]
sonuclar=zip(isimler,notlar)
sonuc_liste=list(sonuclar)  #output->[('ayse cicek', 90), ('elanur sonmez', 59), ('feriha yilmaz', 9)]
print(sonuc_liste)

#map(): fonksiyonu listedeki her elemana uygular
sayilar=[1,2,3,4,5]
sayilarin_karesi_list=list(map(lambda x:x**2 , sayilar))
print(sayilarin_karesi_list) """


#filter():kosula göre fitreleme yapar
sayilar=[1,2,3,4,5,6,7,8]
cift_sayilar=list(filter(lambda x:x%2==0,sayilar))
print(cift_sayilar)
