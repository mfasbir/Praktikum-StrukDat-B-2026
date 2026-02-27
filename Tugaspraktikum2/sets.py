# ======================================
# Praktikum Struktur Data
# Materi: Python Sets
# ======================================

# SET adalah struktur data untuk menyimpan beberapa item
# Set bersifat TIDAK BERURUTAN (unordered),
# TIDAK TERINDEKS, dan TIDAK MEMPERBOLEHKAN DUPLIKAT

# ------------------------------------------------------
# 1. Membuat dan Mengakses Set
# Fungsi:
# - Membuat set dengan beberapa nilai
# - Mengakses item menggunakan perulangan (loop)
# ------------------------------------------------------
myset = {"apel", "pisang", "ceri"}
print("Isi set:")
for x in myset:
    print(x)
# Urutan output bisa berbeda setiap kali dijalankan


# ------------------------------------------------------
# 2. Menambah Item Set
# Fungsi:
# - Menambahkan item baru ke dalam set
# - Jika item sudah ada, maka akan diabaikan
# ------------------------------------------------------
thisset = {"apel", "pisang", "ceri"}
thisset.add("mangga")
print("Setelah ditambah:", thisset)


# ------------------------------------------------------
# 3. Menghapus Item Set
# Fungsi:
# - Menghapus item tertentu dari set
# - remove() akan error jika item tidak ada
# - discard() tidak akan error
# ------------------------------------------------------
thisset.remove("pisang")
print("Setelah dihapus:", thisset)


# ------------------------------------------------------
# 4. Join Set
# Fungsi:
# - Menggabungkan dua set menjadi satu set baru
# - Menggunakan method union()
# ------------------------------------------------------
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print("Hasil join set:", set3)


# ------------------------------------------------------
# 5. Operasi Set (Intersection)
# Fungsi:
# - Mengambil item yang sama pada dua set
# ------------------------------------------------------
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print("Hasil intersection:", z)
