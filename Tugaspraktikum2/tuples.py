# ======================================
# Praktikum Struktur Data
# Materi: Python Tuples
# ======================================

# TUPLE adalah struktur data untuk menyimpan beberapa item
# dalam satu variabel dan bersifat TIDAK DAPAT DIUBAH (immutable)

# ------------------------------------------------------
# 1. Membuat dan Mengakses Tuple
# Fungsi:
# - Membuat tuple dengan beberapa nilai
# - Mengambil nilai tertentu menggunakan indeks
# ------------------------------------------------------
mytuple = ("apel", "pisang", "ceri")
print("Akses indeks ke-0:", mytuple[0])  
# mytuple[0] mengambil elemen pertama karena indeks dimulai dari 0


# ------------------------------------------------------
# 2. Update Tuple (dengan konversi ke list)
# Fungsi:
# - Menunjukkan bahwa tuple tidak bisa diubah langsung
# - Perubahan dilakukan dengan mengubah tuple ke list
# ------------------------------------------------------
x = ("apel", "pisang", "ceri")
y = list(x)          # Mengubah tuple menjadi list agar bisa diubah
y[1] = "kiwi"        # Mengubah elemen indeks ke-1 pada list
x = tuple(y)         # Mengubah kembali list menjadi tuple
print("Tuple setelah diubah:", x)


# ------------------------------------------------------
# 3. Unpacking Tuple
# Fungsi:
# - Memecah isi tuple ke dalam beberapa variabel
# - Setiap variabel menerima satu nilai dari tuple
# ------------------------------------------------------
fruits = ("apel", "pisang", "ceri")
a, b, c = fruits     # Proses unpacking tuple
print("Hasil unpacking:")
print("a =", a)
print("b =", b)
print("c =", c)


# ------------------------------------------------------
# 4. Looping Tuple
# Fungsi:
# - Menampilkan seluruh isi tuple satu per satu
# - Menggunakan perulangan for
# ------------------------------------------------------
print("Isi tuple:")
for item in fruits:
    print(item)


# ------------------------------------------------------
# 5. Join Tuple
# Fungsi:
# - Menggabungkan dua tuple menjadi satu tuple baru
# - Menggunakan operator tambah (+)
# ------------------------------------------------------
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print("Hasil join tuple:", tuple3)


# ------------------------------------------------------
# 6. Method Tuple
# Fungsi:
# - count(): menghitung jumlah kemunculan suatu nilai
# - index(): mencari posisi indeks pertama suatu nilai
# ------------------------------------------------------
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

jumlah_5 = thistuple.count(5)   # Menghitung berapa kali angka 5 muncul
index_8 = thistuple.index(8)    # Mencari indeks pertama angka 8

print("Jumlah angka 5:", jumlah_5)
print("Index pertama angka 8:", index_8)
