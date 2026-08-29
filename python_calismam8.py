"""ogrenci_isimleri=["ayse","fatma","eren","betul","hamza","yakup"]
ogrenci_numaralari=[125,120,180,112,190,98]
max_ogrenci_numarasi=0
max_sahibi=""
min_ogrenci_numarasi=1000
min_sahibi=""
for x in range(len(ogrenci_numaralari)): #listede 6 eleman olduğunu soyler ve range(6) bize sırasıyla bunları verir
    if ogrenci_numaralari[x]>max_ogrenci_numarasi:
        max_ogrenci_numarasi=ogrenci_numaralari[x]
        max_sahibi=ogrenci_isimleri[x]

print("en yuksek okul numarasi: ",max_ogrenci_numarasi,"sahibi",max_sahibi)        
for numara in range(len(ogrenci_numaralari)):
    if ogrenci_numaralari[x]<min_ogrenci_numarasi:
        min_ogrenci_numarasi=ogrenci_numaralari[x]
        min_sahibi=ogrenci_isimleri[x]
print("en dusuk okul numarasi: ",min_ogrenci_numarasi,"sahibi",min_sahibi) """



#daha basiy ibr yolu da var
ogrenci_isimleri=["ayse","fatma","eren","betul","hamza","yakup"]
ogrenci_numaralari=[125,120,180,112,190,98]
max_numara=max(ogrenci_numaralari) #190 max ile direkt listedeki en buyuk sayiyi bulduk
max_index=ogrenci_numaralari.index(max_numara)
max_ogrenci=ogrenci_isimleri[max_index]#max ogrencinin isimini atsdık
min_numara=min(ogrenci_numaralari)#98
min_index=ogrenci_numaralari.index(min_numara)
min_ogrenci=ogrenci_isimleri[min_index]

print(" max ogrenci numarasi:",max_numara,"sahibi",max_ogrenci)
print(" min ogrenci numarasi:",min_numara,"sahibi",min_ogrenci)