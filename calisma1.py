karakter= input("lutfen karakterin adini girin: ")
sehir= input("lutfen yasadigi sehiri belirtin: ")
hikaye_metni= f"""
{karakter} , sabah erkenden uyanip {sehir} sokaklarinda yürümeye 
başladi.Güneş yeni doguyordu ve hava hafif serindi.Küçük bir kafe bulup
 sicak bir çay itti.Birden disarida bir kopek havlamaya basladi.
 Merakla disari çikip kopegin yanina gitti.Kopek ona dostça bakti ve kuyrugunu salladi.
  {karakter}, köpeğin aç olabileceğini düşündü.Hemen bir firina gidip biraz ekmek aldi.Kopege 
  uzattiginda kopek hizla yedi. Bu olay {karakter}'i mutlu etti.
  Gunun geri kalaninda sehrin güzel yerlerini kesfetti.karakter, {sehir}'in ne kadar guzel oldugunu dusundu.
  Akşam olunca eve dönmek için yurumeye basladi.Yolda eski bir arkadasini gordu.
  Arkadasiyla kahve icip sohbet etti.Sonra eve donerken gokyüzune bakti.
  Yildizlar parliyordu ve {karakter} huzur doluydu."""
print(hikaye_metni)
'''f-string bu metnin icinde degisken kullanilacagini belirtir. uc tane tırkan isareti  ise birden fazla kelime
 kullanabilmek at satirlara gecmek icin kullanilir.
 # f olmadan:
print("Merhaba {karakter}")  # Çikti: Merhaba {karakter}

# f-string ve süslü parantez ile:
print(f"Merhaba {karakter}") # Çikti: Merhaba Ahmet
 
 '''


