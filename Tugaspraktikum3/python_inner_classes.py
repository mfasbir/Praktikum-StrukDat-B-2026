# ==========================================
# PYTHON INNER CLASSES (Kelas Bersarang)
# ==========================================

# Inner class adalah class yang didefinisikan di dalam class lain.
# Ini berguna jika Anda ingin mengelompokkan class yang hanya digunakan di satu tempat,
# sehingga kode lebih terorganisir dan memiliki konsep enkapsulasi yang lebih tinggi.

# Outer Class (Class Luar)
class Computer:
  def __init__(self, brand):
    self.brand = brand
    # Membuat objek dari Inner Class di dalam __init__ Outer Class
    self.cpu = self.CPU("Intel Core i7", "3.8 GHz")
    self.ram = self.RAM("16GB")

  def show_specs(self):
    print(f"Komputer {self.brand}")
    self.cpu.show_cpu()
    self.ram.show_ram()

  # Inner Class 1
  class CPU:
    def __init__(self, name, speed):
      self.name = name
      self.speed = speed

    def show_cpu(self):
      print(f"  - CPU: {self.name} ({self.speed})")

  # Inner Class 2
  class RAM:
    def __init__(self, size):
      self.size = size

    def show_ram(self):
      print(f"  - RAM: {self.size}")

# Membuat objek dari class Computer (yang otomatis membuat objek CPU dan RAM di dalamnya)
my_pc = Computer("Asus")
my_pc.show_specs()

# Output:
# Komputer Asus
#   - CPU: Intel Core i7 (3.8 GHz)
#   - RAM: 16GB