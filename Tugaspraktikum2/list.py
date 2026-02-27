# ======================================
# Praktikum Struktur Data
# Materi: Python Lists
# ======================================

# LIST adalah struktur data untuk menyimpan beberapa item
# dalam satu variabel dan bersifat DAPAT DIUBAH (mutable)

# ------------------------------------------------------
# 1. Membuat dan Mengakses List
# Fungsi:
# - Membuat list dengan beberapa nilai
# - Mengakses nilai tertentu menggunakan indeks
# ------------------------------------------------------
thislist = ["apel", "pisang", "ceri"]
print("Akses indeks ke-1:", thislist[1])
# Indeks dimulai dari 0, sehingga indeks ke-1 adalah item kedua


# ------------------------------------------------------
# 2. Mengubah Item List
# Fungsi:
# - Mengubah nilai item pada list menggunakan indeks
# ------------------------------------------------------
thislist[1] = "mangga"
print("Setelah diubah:", thislist)


# ------------------------------------------------------
# 3. Menambah Item List
# Fungsi:
# - Menambahkan item baru ke dalam list
# - append() menambah di akhir list
# - insert() menambah di posisi tertentu
# ------------------------------------------------------
thislist.append("jeruk")      # Menambah di akhir list
thislist.insert(1, "lemon")   # Menambah di indeks ke-1
print("Setelah ditambah:", thislist)


# ------------------------------------------------------
# 4. Menghapus Item List
# Fungsi:
# - Menghapus item berdasarkan nilai atau indeks
# - remove() berdasarkan nilai
# - pop() berdasarkan indeks
# ------------------------------------------------------
thislist.remove("lemon")
thislist.pop(1)
print("Setelah dihapus:", thislist)


# ------------------------------------------------------
# 5. Looping List
# Fungsi:
# - Menampilkan seluruh isi list satu per satu
# - Menggunakan perulangan for
# ------------------------------------------------------
print("Isi list:")
for x in thislist:
    print(x)


# ------------------------------------------------------
# 6. List Comprehension
# Fungsi:
# - Membuat list baru dari list lama secara singkat
# - Menyaring data sesuai kondisi tertentu
# ------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
newlist = [x for x in fruits if "a" in x]
print("Hasil list comprehension:", newlist)


# ------------------------------------------------------
# 7. Sort List
# Fungsi:
# - Mengurutkan isi list secara alfabet (ascending)
# ------------------------------------------------------
thislist.sort()
print("Setelah diurutkan:", thislist)


# ------------------------------------------------------
# 8. Copy List
# Fungsi:
# - Menyalin list tanpa membuat referensi yang sama
# ------------------------------------------------------
mylist = thislist.copy()
print("Hasil copy list:", mylist)


# ------------------------------------------------------
# 9. Join List
# Fungsi:
# - Menggabungkan dua list menjadi satu list baru
# ------------------------------------------------------
list1 = ["a", "b"]
list2 = [1, 2]
list3 = list1 + list2
print("Hasil join list:", list3)
