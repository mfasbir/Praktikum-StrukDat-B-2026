# ==========================================
# PYTHON CLASS METHODS
# ==========================================

# Objek juga dapat berisi metode (methods).
# Metode dalam objek pada dasarnya adalah fungsi yang dimiliki oleh objek tersebut.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # Ini adalah sebuah metode
  def greet(self):
    print("Halo semuanya, perkenalkan nama saya " + self.name)
    
  # Ini adalah metode lain yang menggunakan umur
  def get_birth_year(self, current_year):
    return current_year - self.age

p1 = Person("Fasbir", 30)

# Memanggil metode dari objek
p1.greet() 
# Output: Halo semuanya, perkenalkan nama saya Fasbir

# Memanggil metode yang mengembalikan nilai
tahun_lahir = p1.get_birth_year(2023)
print("Fasbir lahir sekitar tahun:", tahun_lahir) 
# Output: Fasbir lahir sekitar tahun: 1993