# ==========================================
# PYTHON POLYMORPHISM (Polimorfisme)
# ==========================================

# Kata "polymorphism" berarti "banyak bentuk".
# Dalam pemrograman, ini merujuk pada metode/fungsi/operator dengan nama yang sama 
# yang dapat dieksekusi pada banyak objek atau class yang berbeda.

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Berkendara di jalan!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Berlayar di air!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Terbang di udara!")

# Membuat objek dari masing-masing class
car1 = Car("Toyota", "Avanza")       
boat1 = Boat("Yamaha", "Touring") 
plane1 = Plane("Boeing", "747")     

# Menggunakan nama metode yang SAMA yaitu 'move()'
# pada objek dari class yang berbeda-beda. Ini adalah bentuk Polimorfisme.
for x in (car1, boat1, plane1):
  print(x.brand, x.model, end=": ")
  x.move()