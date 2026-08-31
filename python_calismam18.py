#python modul ve paket kavramları
# Modül (module): Tek başına bir .py dosyasıdır. İçinde bir veya birden 
# fazla fonksiyon, sınıf veya değişken tanımı barındırabilir. (Ör. Math 
# modülü, random modülü)

# Paket (package): Bir klasör (dizin) içinde birden fazla modül (.py 
# dosyası) bulunur. Paket içinde her bir .py dosyası kendi başına bir 
# modül olarak kabul edilir. (Ör. Pandas paketi, Numpy paketi)


# ================= PIP (Pip Installs Packages) =================

# pip, Python'un resmi paket (modül) yönetim aracıdır. Python 
# projelerine eklemek istediğimiz kütüphane ve paketleri internetten 
# indirip kurmamızı (install), ayrıca güncellememizi ve kaldırmamızı 
# (uninstall) kolayca sağlar.

import pyjokes
#rastgele bi espri alalim
print(pyjokes.get_joke())
