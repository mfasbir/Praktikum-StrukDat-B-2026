# ==========================================
# PYTHON INHERITANCE (Pewarisan)
# ==========================================

# Inheritance (Pewarisan) memungkinkan kita untuk mendefinisikan sebuah class 
# yang mewarisi semua metode dan properti dari class lain.
# Parent class (Kelas Induk): class yang diwarisi (Base class).
# Child class (Kelas Anak): class yang mewarisi dari class lain (Derived class).

# 1. Membuat Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

# 2. Membuat Child Class
# Untuk membuat class yang mewarisi fungsionalitas dari class lain, 
# masukkan class induk sebagai parameter saat membuat class anak:
class Student(Person):
  def __init__(self, fname, lname, year):
    # super() digunakan untuk memanggil fungsi __init__ dari parent class
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Selamat datang", self.firstname, self.lastname, "di angkatan", self.graduationyear)

x = Student("Fasbir", "Sabran", 2025)
x.printname() # Output: Fasbir Sabran (Metode ini diwarisi dari class Person)
x.welcome()   # Output: Selamat datang Fasbir Sabran Jamil di angkatan 2025