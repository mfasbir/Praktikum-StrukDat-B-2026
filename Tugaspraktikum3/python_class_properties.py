# ==========================================
# PYTHON CLASS PROPERTIES
# ==========================================

# Properti (Properties) pada dasarnya adalah variabel yang menempel pada sebuah objek.
# Dapat mengubah (memodifikasi) properti pada objek, atau bahkan menghapusnya.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Fasbir", 40)

# 1. Memodifikasi Properti Objek
# Kita bisa mengubah umur Fasbir menjadi 41
p1.age = 41
print("Umur Fasbir sekarang:", p1.age) # Output: 41

# 2. Menghapus Properti Objek
# Dapat menghapus properti pada objek dengan menggunakan kata kunci 'del'
del p1.age
# print(p1.age) # Jika baris ini dijalankan, akan menghasilkan Error karena properti 'age' sudah dihapus

# 3. Menghapus Objek Sepenuhnya
# Bisa menghapus objek p1 secara keseluruhan
del p1
# print(p1) # Ini juga akan Error karena p1 sudah tidak ada