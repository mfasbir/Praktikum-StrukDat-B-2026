# ==========================================
# PYTHON ENCAPSULATION (Enkapsulasi)
# ==========================================

# Enkapsulasi adalah konsep membungkus data dan metode yang bekerja pada data dalam satu unit.
# Ini juga membatasi akses langsung ke beberapa komponen objek,
# untuk mencegah modifikasi data yang tidak disengaja.
# Di Python, kita menggunakan awalan garis bawah '_' (protected) atau '__' (private).

class BankAccount:
  def __init__(self, owner, balance):
    self.owner = owner
    # Menggunakan double underscore '__' membuatnya menjadi atribut 'private' (rahasia)
    self.__balance = balance 

  def deposit(self, amount):
    if amount > 0:
      self.__balance += amount
      print(f"Setoran berhasil. Saldo saat ini: {self.__balance}")

  def get_balance(self):
    # Data private hanya bisa diakses dari dalam metode class ini sendiri
    return self.__balance

akun = BankAccount("Rina", 1000)
akun.deposit(500)

# Jika kita mencoba mengakses '__balance' secara langsung, Python akan menghasilkan Error:
# print(akun.__balance) # ERROR: 'BankAccount' object has no attribute '__balance'

# Cara yang benar untuk melihat saldo adalah melalui metode yang disediakan:
print("Saldo akhir:", akun.get_balance())