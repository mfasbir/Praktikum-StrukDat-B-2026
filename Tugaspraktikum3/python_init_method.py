# ==========================================
# PYTHON __init__() METHOD
# ==========================================

# Contoh di atas (MyClass) adalah class yang sangat sederhana dan tidak terlalu berguna di dunia nyata.
# Untuk memahami arti sebenarnya dari class, kita harus memahami fungsi bawaan __init__().
# Semua class memiliki fungsi bernama __init__(), yang selalu dieksekusi saat class tersebut mulai dibuat (diinisiasi).
# Gunakan fungsi __init__() untuk memberikan nilai pada properti objek.

class Person:
  # Fungsi __init__ ini akan otomatis dipanggil saat kita membuat objek baru
  def __init__(self, name, age):
    self.name = name
    self.age = age

# Membuat objek dari class Person dan mengirimkan nilai nama dan umur
p1 = Person("Fasbir", 36)

# Mengakses nilai yang sudah disimpan di dalam objek
print(p1.name) # Output: Fasbir
print(p1.age)  # Output: 36

# Catatan: Fungsi __init__() dipanggil secara otomatis setiap kali objek baru dari class tersebut dibuat.