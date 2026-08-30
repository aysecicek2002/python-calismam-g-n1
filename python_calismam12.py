#FONKSIYONLAR 
#pythonda fonksiyonlar def ile tanimlanir. fonlsiyonlar tekrar tekrar cagirilabilirler.
""" def ekrana_yazma_fonksiyonu():
    print("selamlar")
    print("nasilsiniz") #isimiz bitti donguden cıkıyoruz
ekrana_yazma_fonksiyonu()  #istedigimiz kadar cagirabiliriz
ekrana_yazma_fonksiyonu()
ekrana_yazma_fonksiyonu()
ekrana_yazma_fonksiyonu()
ekrana_yazma_fonksiyonu()
#fonksiyonların parametre alması ve geri deger dondurmesi
def ekrana_yazma_fonksiyonu(isim):
    print("selamlar",isim)
    print("nasilsiniz") 
ekrana_yazma_fonksiyonu("ayse")  #fonskiyonlarda bu sekılde kullanabilşriz
ekrana_yazma_fonksiyonu("fatma")
ekrana_yazma_fonksiyonu("selin")
ekrana_yazma_fonksiyonu("gokdeniz")
ekrana_yazma_fonksiyonu("yemliha")


def ekrana_yazma_fonksiyonu(isim2):
    print(type(isim2))
    print("selamlar",isim2)
    print("nasilsiniz")              
isim2="ayse"
ekrana_yazma_fonksiyonu("ayse")  
ekrana_yazma_fonksiyonu(1)  
#output 
#<class 'str'>
#selamlar ayse
#nasilsiniz
#<class 'int'>
#selamlar 1
#nasilsiniz  
"""
"""
def topla(a,b):
    print("sayilarin toplami:",a+b)
topla(100,1234)    #ya da


def topla(d,c):
    toplam=d+c
    print("sayilarin toplami:",toplam)
topla(100,1234)    #!!!! aynı sey aslında

def topla(e,f):
    print("sayilarin toplami:",e+f)
def carp(x,y):
   return x*y #burada return kullsndigimiz icin islemi yap ve gec gibi gorur
topla(24,34)   #bu yuzden islemi yaptıgımız zaman cağırdıgımız fonksiyonu print
print(carp(3,4)) #ile yazdiracagiz sonucu görebilmek icin
carp(8,9) """


#scop(kapsam)
"""
def ornek1():
    x=4 #yerel degisken
    print("yerel degisken:",x)
x=10 #global degisken
print("global degisken:",x)#10
ornek1() #4 """

def ornek1():
    x=4 #yerel degisken
    print("yerel degisken:",x) 

def ornek2():
    global x 
    x=x*5
    print("global x:",x)
x=10 #global x yaparak burayi da degistirme yetkisi verdi bununda print sonucu 50 olur.
ornek1()
ornek2()    
print(x)


#bolme ve cikarma ama eğer bölen 0 sa bölünmesin

def bolme(a,b):
    if b>0:
        bolum_sonucu=a/b
        print("bolme islemi sonucu:",bolum_sonucu)
    elif b==0:
        print("bolme islemi yapilamaz")
def cikarma(a,b):
    cikarma_sonucu=a-b
    print("cikarma sonucu:",cikarma_sonucu)
bolme(10,2)
cikarma(10,2)
bolme(10,0)